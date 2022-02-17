from django.db.models.query import QuerySet
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.views.generic import FormView, TemplateView
from .models import About, Carousel, CompanyDetails, Instructors, Passplus, Service, TeachingHours, Terms, Testimonial
from blog.models import Post
from .forms import ContactForm


# Create your views here.
class AboutUsPage(generic.ListView):
    """ About Us Page view """
    model = About
    queryset = About.objects.filter(status=1).order_by("-created_at")[0:1]
    template_name = "pages/about-us.html"

    def get_context_data(self, **kwargs):
        """ Returns the Instructors list and Company Contact info """
        context = super().get_context_data(**kwargs)
        context['instructors_list'] = Instructors.objects.filter(status=1).order_by("name")
        return context

    def aboutuspage(self, request):
        """ Return render view for about page """
        return render(request, 'pages/about-us.html')


class ContactUsPage(FormView):
    """ Contact Us Page view """
    template_name = "pages/contact-us.html"
    form_class = ContactForm
    success_url = reverse_lazy('pages/success')

    def form_valid(self, form):
        """ If form is valid sends the form """
        # Calls the custom send method
        form.send()
        # This will add the flash message after email being valid
        # messages.success(self.request, "Message sent." )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """ Returns the instructors list, Teaching Hours and Company Contact info """
        context = super().get_context_data(**kwargs)
        context['companydetails'] = CompanyDetails.objects.all()[0:1]
        context['teaching_hours_list'] = TeachingHours.objects.all().order_by("id")
        return context


class ContactSuccessView(TemplateView):
    """ If the contact form was valid this page is returned to view """
    template_name = "pages/success.html"


class InstructorsList(generic.ListView):
    """ retrieves a list of the Instructors """
    model = Instructors
    queryset = Instructors.objects.filter(status=1).order_by("name")


class PassPlusPage(generic.ListView):
    """ Pass Plus Page view"""

    model = Passplus
    queryset = Passplus.objects.filter(status=1).order_by("-created_at")[0:1]
    template_name = "pages/pass-plus.html"


class PricesPage(generic.ListView):
    """ Prices Page view"""

    model = Service
    queryset = Service.objects.all().order_by("price")
    template_name = "pages/prices.html"

    def get_context_data(self, **kwargs):
        """ Returns the featured prices """
        context = super().get_context_data(**kwargs)
        context['featured_list'] = Service.objects.filter(featured=1).order_by("price")
        return context


class TermsPage(generic.ListView):
    """ Terms and Conditions view"""
    model = Terms
    queryset = Terms.objects.filter(status=1).order_by("-created_at")[0:1]
    template_name = "pages/terms-and-conditions.html"


class Testimonials(generic.ListView):
    """ Returns the latest Testimonials for the home Page """
    model = Testimonial
    queryset = Testimonial.objects.filter(status=1).order_by("-created_at")
    template_name = "index.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        """ Returns the instructors list and Company Contact info """
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.order_by("-created_at")[0:3]
        context['carousel_list'] = Carousel.objects.filter(include_in_carousel=1).order_by("slide_identifying_name")
        return context


def social_icons_list(request):
    """ Returns the Company Contact info """
    social_icons_list = CompanyDetails.objects.all()[0:1]
    context = {
        'social_icons_list': social_icons_list,
    }
    return context


from django.db.models.query import QuerySet
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import FormView, TemplateView
from .models import (
    About,
    Carousel,
    CompanyDetails,
    Instructors,
    Passplus,
    Service,
    TeachingHours,
    Terms,
    Testimonial,
)
from blog.models import Post
from .forms import ContactForm


# Create your views here.
class AboutUsPage(generic.ListView):
    """
    Render the about us page.
    """
    model = About
    queryset = About.objects.filter(status=1).order_by("-created_at")[0:1]
    template_name = "pages/about-us.html"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the instructor page.
        """
        context = super().get_context_data(**kwargs)
        context["instructors_list"] = Instructors.objects.filter(status=1).order_by(
            "name"
        )
        return context

    def aboutuspage(self, request):
        """
        Render the about us page.
        @param request - the request object
        @returns the about us page
        """
        return render(request, "pages/about-us.html")


class ContactUsPage(FormView):
    """
    The contact us page. This page is used to send emails to the company.
    """
    template_name = "pages/contact-us.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact-us")

    def form_valid(self, form):
        """
        Override the form_valid method to send the form to the server.
        """
        # Calls the custom send method
        form.send()
        # This will add the flash message after email being valid
        messages.success(self.request, "Message sent.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Get the context data for the page.
        This is used to pass data to the template.
        """
        context = super().get_context_data(**kwargs)
        context["companydetails"] = CompanyDetails.objects.all()[0:1]
        context["teaching_hours_list"] = TeachingHours.objects.all().order_by("id")
        return context


class ContactSuccessView(TemplateView):
    """
    The contact success page.
    """
    template_name = "pages/success.html"


class InstructorsList(generic.ListView):
    model = Instructors
    queryset = Instructors.objects.filter(status=1).order_by("name")


class PassPlusPage(generic.ListView):
    """
    The PassPlusPage class is a generic class that is used to display the
    PassPlus page.
    """
    model = Passplus
    queryset = Passplus.objects.filter(status=1).order_by("-created_at")[0:1]
    template_name = "pages/pass-plus.html"


class PricesPage(generic.ListView):
    """
    The view for the prices page.
    This is used to display the featured services.
    """
    model = Service
    queryset = Service.objects.all().order_by("price")
    template_name = "pages/prices.html"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the home page.
        This is used to display the featured services.
        """
        context = super().get_context_data(**kwargs)
        context["featured_list"] = Service.objects.filter(featured=1).order_by(
            "featured_order"
        )
        return context


class TermsPage(generic.ListView):
    """
    The terms and conditions page.
    """
    model = Terms
    queryset = Terms.objects.filter(status=1).order_by("-created_at")[0:1]
    template_name = "pages/terms-and-conditions.html"


class Testimonials(generic.ListView):
    """
    Override the get_context_data method to add the post_list and
    carousel_list to the context dictionary.
    """
    model = Testimonial
    queryset = Testimonial.objects.filter(status=1).order_by("-created_at")
    template_name = "index.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        """
        Override the get_context_data method to add the post_list and
        carousel_list to the context dictionary.
        """
        context = super().get_context_data(**kwargs)
        context["post_list"] = Post.objects.order_by("-created_at")[0:3]
        context["carousel_list"] = Carousel.objects.filter(
            include_in_carousel=1
        ).order_by("slide_identifying_name")
        return context


def social_icons_list(request):
    """
    Return the social icons list for the footer.
    """
    social_icons_list = CompanyDetails.objects.all()[0:1]
    context = {
        "social_icons_list": social_icons_list,
    }
    return context

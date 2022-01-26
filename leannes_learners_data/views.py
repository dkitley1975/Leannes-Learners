from django.db.models.query import QuerySet
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.views.generic import FormView, TemplateView
from .models import About, Blog, Carousel, CompanyDetails, Instructors, Passplus, Service, TeachingHours, Terms, Testimonial
from .forms import CommentForm, ContactForm



# Create your views here.

class AboutUsPage(generic.ListView):
    """ About Us Page view """
    model = About
    queryset = About.objects.filter(status=1).order_by("-created_at")[0:1]
    template_name = "pages/about-us.html"

    def get_context_data(self, **kwargs):
        """ Gets the Instructors list and Company Contact info """
        context = super().get_context_data(**kwargs)
        context['instructors_list'] = Instructors.objects.filter(status=1).order_by("name")
        context['social'] = CompanyDetails.objects.all()[0:1]
        return context

    def aboutuspage(self, request):
        """ Return render view for about page """
        return render(request, 'pages/about-us.html')


class BlogPost(View):
    """ individual Blog Page view """
    def get(self, request, slug, *args, **kwargs):
        """ Return render view for blog post detail """
        queryset = Blog.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)
        comments = blog.comments.filter(approved=True).order_by("-created_at")
        liked = False
        if blog.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "components/blog/post.html",
            {
                "blog": blog,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Blog.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)
        comments = blog.comments.filter(approved=True).order_by("-created_at")
        liked = False
        if blog.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.blog = blog
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "components/blog/post.html",
            {
                "blog": blog,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class BlogPage(generic.ListView):
    """ Blog Page list view """
    model = Blog
    queryset = Blog.objects.filter(status=1).order_by("-created_at")
    template_name = "pages/blog.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        """ Gets the instructors list and Company Contact info """
        context = super().get_context_data(**kwargs)
        context['social'] = CompanyDetails.objects.all()[0:1]
        return context



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
        """ Gets the instructors list, Teaching Hours and Company Contact info """
        context = super().get_context_data(**kwargs)
        context['social'] = CompanyDetails.objects.all()[0:1]
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


class LikePost(View):
    """ Blog post view page like functionality view """

    def post(self, request, slug, *args, **kwargs):
        blog = get_object_or_404(Blog, slug=slug)
        if blog.likes.filter(id=request.user.id).exists():
            blog.likes.remove(request.user)
        else:
            blog.likes.add(request.user)

        return HttpResponseRedirect(reverse('blog-post', args=[slug]))


class PassPlusPage(generic.ListView):
    """ Pass Plus Page view"""

    model = Passplus
    queryset = Passplus.objects.filter(status=1).order_by("-created_at")[0:1]
    template_name = "pages/pass-plus.html"

    def get_context_data(self, **kwargs):
        """ Gets the instructors list and Company Contact info """

        context = super().get_context_data(**kwargs)
        context['social'] = CompanyDetails.objects.all()[0:1]
        return context


class PricesPage(generic.ListView):
    """ Prices Page view"""

    model = Service
    queryset = Service.objects.all().order_by("price")
    template_name = "pages/prices.html"

    def get_context_data(self, **kwargs):
        """ Gets the instructors list and Company Contact info """

        context = super().get_context_data(**kwargs)
        context['featured_list'] = Service.objects.filter(featured=1).order_by("price")
        context['social'] = CompanyDetails.objects.all()[0:1]
        return context


class TermsPage(generic.ListView):
    """ Terms and Conditions view"""

    model = Terms
    queryset = Terms.objects.filter(status=1).order_by("-created_at")[0:1]
    template_name = "pages/terms-and-conditions.html"

    def get_context_data(self, **kwargs):
        """ Gets the instructors list and Company Contact info """

        context = super().get_context_data(**kwargs)
        context['social'] = CompanyDetails.objects.all()[0:1]
        return context


class Testimonials(generic.ListView):
    """ Grabs the latest Testimonials for the home Page """
    model = Testimonial
    queryset = Testimonial.objects.filter(status=1).order_by("-created_at")
    template_name = "index.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        """ Gets the instructors list and Company Contact info """
        context = super().get_context_data(**kwargs)
        context['blog_list'] = Blog.objects.filter(status=1).order_by("-created_at")[0:3]
        context['carousel_list'] = Carousel.objects.filter(include_in_carousel=1).order_by("slide_identifying_name")
        context['social'] = CompanyDetails.objects.all()[0:1]

        return context

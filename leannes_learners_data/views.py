from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic, View
from .models import About, Blog, Carousel, Instructors, Passplus, Service, Testimonial
from .forms import CommentForm


# Create your views here.

class AboutUsPage(generic.ListView):
    model = About
    queryset = About.objects.filter(status=1).order_by("-created_at")[0:1]
    template_name = "about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instructors_list'] = Instructors.objects.filter(status=1).order_by("name")
        return context


class BlogDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Blog.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)
        comments = blog.comments.filter(approved=True).order_by("-created_at")
        liked = False
        if blog.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog_post_view.html",
            {
                "blog": blog,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def BlogPost(self, request, slug, *args, **kwargs):
        queryset = Blog.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)
        comments = blog.comments.filter(approved=True).order_by("-created_at")
        liked = False
        if Blog.likes.filter(id=self.request.user.id).exists():
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
            "blog_post_view.html",
            {
                "blog": blog,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class BlogPage(generic.ListView):
    model = Blog
    queryset = Blog.objects.filter(status=1).order_by("-created_at")
    template_name = "blog.html"
    paginate_by = 9


def contact(request):
    if request.method == "POST":
        contact_first_name = request.POST['contact-first-name']
        contact_last_name = request.POST['contact-last-name']
        contact_postcode = request.POST['contact-postcode']
        contact_email = request.POST['contact-email']
        contact_number = request.POST['contact-number']
        contact_message = request.POST['contact-message']

        return render(request, 'contact.html', {'contact_first_name': contact_first_name })

    else:
        return render(request, 'contact.html', {})

class InstructorsList(generic.ListView):
    model = Instructors
    queryset = Instructors.objects.filter(status=1).order_by("name")


class LikePost(View):

    def post(self, request, slug, *args, **kwargs):
        blog = get_object_or_404(Blog, slug=slug)
        if blog.likes.filter(id=request.user.id).exists():
            blog.likes.remove(request.user)
        else:
            blog.likes.add(request.user)

        return HttpResponseRedirect(reverse('blog_post_view', args=[slug]))


class PassPlusPage(generic.ListView):
    model = Passplus
    queryset = Passplus.objects.filter(status=1).order_by("-created_at")[0:1]
    template_name = "pass_plus.html"


class PricesPage(generic.ListView):
    model = Service
    queryset = Service.objects.all().order_by("price")
    template_name = "prices.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_list'] = Service.objects.filter(featured=1).order_by("price")
        return context


class Testimonials(generic.ListView):
    model = Testimonial
    queryset = Testimonial.objects.filter(status=1).order_by("-created_at")
    template_name = "index.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_list'] = Blog.objects.filter(status=1).order_by("-created_at")[0:3]
        context['carousel_list'] = Carousel.objects.filter(include_in_carousel=1).order_by("slide_identifying_name")
        return context

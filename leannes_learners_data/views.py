from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Blog, Testimonial, Carousel, Pass_plus
from .forms import CommentForm


# Create your views here.


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


class LikePost(View):

    def post(self, request, slug, *args, **kwargs):
        blog = get_object_or_404(Blog, slug=slug)
        if blog.likes.filter(id=request.user.id).exists():
            blog.likes.remove(request.user)
        else:
            blog.likes.add(request.user)

        return HttpResponseRedirect(reverse('blog_post_view', args=[slug]))


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


class Pass_plus(generic.ListView):
    model = Pass_plus
    queryset = Pass_plus.objects.filter(status=1).order_by("-created_at")[0:1]
    template_name = "pass_plus.html"

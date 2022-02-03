from django.db.models.query import QuerySet
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.views.generic import FormView, TemplateView, CreateView
from blog.models import Post
from leannes_learners_data.models import CompanyDetails
from .forms import CommentForm, AddPostForm
from django_summernote.widgets import SummernoteInplaceWidget



# Create your views here.
class BlogPost(View):
    """ individual Blog Page view """
    def get(self, request, slug, *args, **kwargs):
        """ Return render view for blog post detail """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_at")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "pages/blog/post.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_at")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "pages/blog/post.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class BlogPostsPage(generic.ListView):
    """ Blog Page list view """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_at")
    template_name = "pages/blog/blog.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        """ Gets the instructors list and Company Contact info """
        context = super().get_context_data(**kwargs)
        context['social'] = CompanyDetails.objects.all()[0:1]
        return context


class LikePost(View):
    """ Blog post view page like functionality view """

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('blog-post', args=[slug]))


class AddPostSuccess(TemplateView):
    """ If the contact form was valid this page is returned to view """
    template_name = "pages/blog/success_post_submission.html"


class AddPost(CreateView):
    """ Add a new post page """
    model = Post
    template_name = "pages/blog/new_blog_post_entry.html"
    form_class = AddPostForm


    def get_context_data(self, **kwargs):
        """ Gets the Company Contact info """
        context = super().get_context_data(**kwargs)
        context['social'] = CompanyDetails.objects.all()[0:1]
        return context


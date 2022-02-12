from django.db.models.query import QuerySet
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, AccessMixin
from django.contrib.auth import logout

from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django_summernote.widgets import SummernoteInplaceWidget
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic, View
from django.views.generic import CreateView, DeleteView, FormView, ListView, TemplateView, UpdateView

from blog.models import Category, Post
from leannes_learners.settings import LOGIN_URL
from leannes_learners_data.models import CompanyDetails
from .forms import CommentForm, CreateNewPostForm
from django.db.models import Count






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

    def get_context_data(self, **kwargs):
        """ Gets the Company Contact info """
        context = super().get_context_data(**kwargs)
        context['social'] = CompanyDetails.objects.all()[0:1]
        return context

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
        return HttpResponseRedirect(request.path)
        


class BlogPostsPage(generic.ListView):
    """ Blog Page list view """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_at")
    template_name = "pages/blog/blog.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        """ Gets the Company Contact info """
        context = super().get_context_data(**kwargs)
        context['social'] = CompanyDetails.objects.all()[0:1]
        return context


class CategoryListView(ListView):
    template_name = 'pages/blog/category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs
            ['category']).filter(status='1')
        }
        return content


def category_list(request):
    '''
    counts all the categories within the posts and filters those with a count of 0 out
    '''
    category_list = Category.objects.annotate(post_count=Count("post")).filter(post_count__gt=0).order_by('-post_count')
    context = {
        'category_list': category_list,
    }
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


class CreatePostSuccessfull(TemplateView):
    """ If the contact form was valid this page is returned to view """
    template_name = "pages/blog/success-post-submission.html"


class CreatePost(CreateView):
    """ Add a new post page """
    model = Post
    template_name = "pages/blog/create-new-post.html"
    form_class = CreateNewPostForm

    def get_context_data(self, **kwargs):
        """ Gets the Company Contact info """
        context = super().get_context_data(**kwargs)
        context['social'] = CompanyDetails.objects.all()[0:1]
        return context


class UpdatePost(UpdateView):
    """ update post page """
    model = Post
    template_name = "pages/blog/edit-blog-post-entry.html"
    form_class = CreateNewPostForm

    def get_context_data(self, **kwargs):
        """ Gets the Company Contact info """
        context = super().get_context_data(**kwargs)
        context['social'] = CompanyDetails.objects.all()[0:1]
        return context


class DeletePost(DeleteView):
    """ Add a new post page """
    model = Post
    template_name = "pages/blog/delete-blog-post-entry.html"
    success_url = reverse_lazy('blog')

    def get_context_data(self, **kwargs):
        """ Gets the Company Contact info """
        context = super().get_context_data(**kwargs)
        context['social'] = CompanyDetails.objects.all()[0:1]
        return context
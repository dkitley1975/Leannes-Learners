from django.db.models.query import QuerySet
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin, AccessMixin
from django.contrib.auth import logout

from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django_summernote.widgets import SummernoteInplaceWidget
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic, View
from django.views.generic import CreateView, DeleteView, FormView, ListView, TemplateView, UpdateView

from blog.models import Category, Post, Comment
from leannes_learners.settings import LOGIN_URL
from leannes_learners_data.models import CompanyDetails
from .forms import CommentForm, CreateNewPostForm
from django.db.models import Count






# Create your views here.

class BlogPost(View):
    """ individual Blog Page view """
    def get(self, request, slug, *args, **kwargs):
        """ Return render view for blog post detail """
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_at")
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
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_at")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            comment_form = CommentForm()
            return HttpResponseRedirect(request.path)
        else:
            comment_form = CommentForm()

        return render(request,
            "pages/blog/post.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
            },
        )
        
        


class BlogPostsPage(generic.ListView):
    """ Blog Page list view """
    model = Post
    queryset = Post.objects.order_by("-created_at")
    template_name = "pages/blog/blog.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        """ Gets the Company Contact info """
        context = super().get_context_data(**kwargs)
        context['social'] = CompanyDetails.objects.all()[0:1]
        return context


class CategoryListView(ListView):
    """ Category list view for the blog posts"""
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
    """
    counts all the categories within the posts and filters
    those with a count of 0 out
    """
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

class DeleteComment(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ delete a comment """
    model = Comment
    template_name = "pages/blog/delete-blog-comment.html"
    
    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse_lazy('blog-post', args=[slug])

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.name










class LikeComment(LoginRequiredMixin, View):
    """ Comment like functionality """

    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)
        comment_disliked = False
        for disliked in comment.disliked.all():
            if disliked == request.user:
                comment_disliked = True
                break

        if comment_disliked:
            comment.disliked.remove(request.user)

        liked = False

        for liked in comment.liked.all():
            if liked == request.user:
                liked = True
                break

        if not liked:
            comment.liked.add(request.user)

        if liked:
            comment.liked.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class DislikeComment(LoginRequiredMixin, View):
    """
    comment dislike functionality
    """

    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)

        liked = False
        
        for liked in comment.liked.all():
            if liked == request.user:
                liked = True
                break

        if liked:
            comment.liked.remove(request.user)

        comment_disliked = False

        for disliked in comment.disliked.all():
            if disliked == request.user:
                comment_disliked = True
                break

        if not comment_disliked:
            comment.disliked.add(request.user)

        if comment_disliked:
            comment.disliked.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class CommentReplyView(LoginRequiredMixin, View):
    def post(self, request, slug, pk, *args, **kwargs):
        post = Post.objects.get(slug=slug)
        parent_comment = Comment.objects.get(pk=pk)
        comment_form = CommentForm(data=request.POST)
        
        if comment_form.is_valid():
            comment_form.instance.name = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.parent = parent_comment
            comment.save()
            comment_form = CommentForm()
            return HttpResponseRedirect(reverse('blog-post', args=[slug]))
        else:
            comment_form = CommentForm()

        return HttpResponseRedirect(reverse('blog-post', args=[slug]))


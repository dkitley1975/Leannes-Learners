from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.views import generic, View
from django.views.generic import CreateView, DeleteView, FormView, ListView, TemplateView, UpdateView
from django.db.models import Count

from blog.models import Category, Post, Comment
from leannes_learners_data.models import CompanyDetails
from .forms import CommentForm, CreateNewPostForm

# from django.db.models.query import QuerySet
# from django.contrib import messages
# from django.contrib.auth.mixins import PermissionRequiredMixin, AccessMixin
# from django.contrib.auth import logout
# from django.http.response import HttpResponse
# from django_summernote.widgets import SummernoteInplaceWidget
# from leannes_learners.settings import LOGIN_URL
# from django.utils.decorators import method_decorator


# Create your views here.

class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        """
        Get the data for a specific post.
        @param request - the request object
        @param slug - the slug of the post
        @returns the data for the post
        """
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


    def post(self, request, slug, *args, **kwargs):
        """
        Post the results to the database.
        @param results - the results to post
        """
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


class BlogPosts(generic.ListView):
    """
    The blog page. This is a generic list view that displays all the posts in the database.
    """
    model = Post
    queryset = Post.objects.order_by("-created_at")
    template_name = "pages/blog/blog.html"
    paginate_by = 9


class CategoryList(ListView):
    """
    The category list view.
    @param self - the view itself
    @param category - the category name
    @returns the queryset for the category page
    """
    template_name = 'pages/blog/category.html'
    context_object_name = 'catagorylist'

    def get_queryset(self):
        """
        Get the queryset for the category page.
        @param self - the view itself
        @returns the queryset for the category page
        """
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs
            ['category']).filter()
        }
        return content


def category_list(request):
    """
    Return the category list for the category page.
    @param request - the request object
    @returns the category list
    """
    category_list = Category.objects.annotate(post_count=Count("post")).filter(post_count__gt=0).order_by('-post_count')
    context = {
        'category_list': category_list,
    }
    return context


class CommentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a comment from the database.
    @param self - the comment delete view instance
    @returns the success url for the post detail page.
    """
    model = Comment
    template_name = "pages/blog/post-comment-delete.html"
    
    def get_success_url(self):
        """
        Get the success url for the post detail page.
        @param self - the post detail view instance
        @returns the success url for the post detail page.
        """
        slug = self.kwargs['slug']
        return reverse_lazy('post-detail', args=[slug])

    def test_func(self):
        """
        Test function for the test function.
        @returns True if the user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.name




class CommentDislike(View):
    """
    This function is used to like or dislike a comment. It is called when the user clicks on the like or dislike button.
    @param request - the request object
    @param slug - the slug of the post
    @param pk - the primary key of the comment
    @returns a redirect to the post detail page
    """
    def post(self, request, slug, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)
        if comment.disliked.filter(id=request.user.id).exists():
            comment.disliked.remove(request.user)
        else:
            comment.disliked.add(request.user)
            if comment.liked.filter(id=request.user.id).exists():
                comment.liked.remove(request.user)
        return HttpResponseRedirect(reverse('post-detail', args=[slug]))


class CommentLike(View):
    """
    This function is used to like or dislike a comment. It is called when a user clicks on the like button.
    @param request - the request object
    @param slug - the slug of the post
    @param pk - the primary key of the comment
    @returns a redirect to the post detail page
    """
    def post(self, request, slug, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)
        if comment.liked.filter(id=request.user.id).exists():
            comment.liked.remove(request.user)
        else:
            comment.liked.add(request.user)
            if comment.disliked.filter(id=request.user.id).exists():
                comment.disliked.remove(request.user)
        return HttpResponseRedirect(reverse('post-detail', args=[slug]))


class CommentReply(LoginRequiredMixin, View):
    def post(self, request, slug, pk, *args, **kwargs):
        """
        Post a comment on a post.
        @param request - the request object
        @param slug - the slug of the post
        @param pk - the primary key of the comment
        @returns the post detail page
        """
        post = Post.objects.get(slug=slug)
        parent_comment = Comment.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comment_form.instance.name = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.parent = parent_comment
            comment.save()
            comment_form = CommentForm()
            return HttpResponseRedirect(reverse('post-detail', args=[slug]))
        else:
            comment_form = CommentForm() 

        return HttpResponseRedirect(reverse('post-detail', args=[slug]))


class PostCreate(CreateView):
    """
    The view for creating a new post.
    @param CreateView - the view for creating a new post.
    """
    model = Post
    template_name = "pages/blog/post-creation.html"
    form_class = CreateNewPostForm


class PostDelete(DeleteView):
    """
    Delete a post from the database.
    @param DeleteView - the delete view class
    @param Post - the post model class
    @param template_name - the template name for the delete page
    @param success_url - the url to redirect to after deletion
    """
    model = Post
    template_name = "pages/blog/post-entry-delete.html"
    success_url = reverse_lazy('blog')


class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        """
        When a user likes a post, we want to add them to the likes list of the post.
        @param request - the request object
        @param slug - the slug of the post
        @returns the redirect to the post detail page
        """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post-detail', args=[slug]))


class PostUpdate(UpdateView):
    """
    The view for editing a post.
    @param model - the model we are editing.
    @param template_name - the template we are using.
    @param form_class - the form we are using.
    """
    model = Post
    template_name = "pages/blog/post-entry-edit.html"
    form_class = CreateNewPostForm

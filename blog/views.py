from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.views import generic, View
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)
from django.db.models import Count

from blog.models import Category, Post, Comment
from .forms import CommentForm, CreateNewPostForm

# Create your views here.


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        """
        Get the data for a specific post.
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
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Render the post page.
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

        return render(
            request,
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
    The blog page. This is a generic list view that 
    displays all the posts in the database.
    """

    model = Post
    queryset = Post.objects.order_by("-created_at")
    template_name = "pages/blog/blog.html"
    paginate_by = 9


class CategoryList(ListView):
    """
    The category list view.
    """
    model = Category
    template_name = "pages/blog/category.html"
    context_object_name = "categorylist"

    def get_queryset(self):
        """
        Get the queryset for the category page.
        """
        content = {
            "cat": self.kwargs["category"],
            "posts": Post.objects.filter(
                category__slug=self.kwargs["category"]
            ).filter(),
            "title": self.kwargs["category"].replace("-", " "),
        }
        return content


def category_list(request):
    """
    Return the category list for the category list page.
    """
    category_list = (
        Category.objects.annotate(post_count=Count("post"))
        .filter(post_count__gt=0)
        .order_by("-post_count")
    )
    context = {"category_list": category_list}
    return context


class CommentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Test function for the test function.
    @returns True if the user is the author of the comment
    or if the user is a member of staff.
    """
    model = Comment
    template_name = "pages/blog/post-comment-delete.html"

    def get_success_url(self):
        """
        Get the success url for the post detail view.
        """
        slug = self.kwargs["slug"]
        return reverse_lazy("post-detail", args=[slug])

    def test_func(self):
        """
        Check if the user is a staff member. 
        If so, return true. Otherwise, return false.
        """
        comment = self.get_object()
        if self.request.user.is_staff:
            return self.request.user.is_staff
        else:
            return self.request.user == comment.name


class CommentDislike(View):
    """
    This function is used to like or dislike a comment.
    It is called when the user clicks on the like or dislike button.
    """
    def post(self, request, slug, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)
        if comment.disliked.filter(id=request.user.id).exists():
            comment.disliked.remove(request.user)
        else:
            comment.disliked.add(request.user)
            if comment.liked.filter(id=request.user.id).exists():
                comment.liked.remove(request.user)
        return HttpResponseRedirect(reverse("post-detail", args=[slug]))


class CommentLike(View):
    """
    This function is used to like or dislike a comment.
    It is called when a user clicks on the like button.
    """
    def post(self, request, slug, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)
        if comment.liked.filter(id=request.user.id).exists():
            comment.liked.remove(request.user)
        else:
            comment.liked.add(request.user)
            if comment.disliked.filter(id=request.user.id).exists():
                comment.disliked.remove(request.user)
        return HttpResponseRedirect(reverse("post-detail", args=[slug]))


class CommentReply(LoginRequiredMixin, View):
    def post(self, request, slug, pk, *args, **kwargs):
        """
        This function is used to post a comment on a post.
        It takes the request, the slug of the post,
        the primary key of the comment, and the comment form.
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
            return HttpResponseRedirect(reverse("post-detail", args=[slug]))
        else:
            comment_form = CommentForm()

        return HttpResponseRedirect(reverse("post-detail", args=[slug]))


class PostCreate(CreateView):
    """
    The view for creating a new post.
    """
    model = Post
    template_name = "pages/blog/post-creation.html"
    form_class = CreateNewPostForm


class PostDelete(DeleteView):
    """
    Delete a post from the database.
    """
    model = Post
    template_name = "pages/blog/post-entry-delete.html"
    success_url = reverse_lazy("blog")


class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        """
        When a user likes a post,
        we want to add them to the likes list of the post.
        """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse("post-detail", args=[slug]))


class PostUpdate(UpdateView):
    """
    The view for editing a post.
    """
    model = Post
    template_name = "pages/blog/post-entry-edit.html"
    form_class = CreateNewPostForm

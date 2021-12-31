from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Blog
# Create your views here.


class BlogList(generic.ListView):
    model = Blog
    queryset = Blog.objects.filter(status=1).order_by("-created_at")
    template_name = "index.html"
    paginate_by = 6


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
            },
        )

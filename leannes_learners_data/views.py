from django.shortcuts import render
from django.views import generic
from .models import Blog
# Create your views here.


class BlogList(generic.ListView):
    model = Blog
    queryset = Blog.objects.filter(status=1).order_by("-created_at")
    template_name = "index.html"
    paginate_by = 6

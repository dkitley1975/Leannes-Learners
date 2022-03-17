from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    """
    The comment form for the comment section of the website.
    """

    class Meta:
        model = Comment
        fields = ("comment",)


class CreateNewPostForm(forms.ModelForm):
    """
    Create a form for creating a new post. 
    This is used in the admin site.
    """

    class Meta:
        model = Post
        fields = (
            "title",
            "featured_image",
            "alt_tag",
            "content",
            "excerpt",
            "author",
            "category",
        )
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "alt_tag": forms.TextInput(attrs={"class": "form-control"}),
            "excerpt": forms.Textarea(attrs={"class": "form-control"}),
            "content": SummernoteWidget(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }

from email.policy import default
from .models import Comment, Post
from django import forms



class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)



class AddPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ( 
			'title', 
			'featured_image',
			'alt_tag',
			'content',
			'excerpt',
			'author',
			'status',
			# 'slug'
			) 

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'alt_tag': forms.TextInput(attrs={'class': 'form-control'}),
			'content': forms.Textarea(attrs={'class': 'form-control'}),
			'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
			'author': forms.Select(attrs={'class': 'form-control'}),
			'status': forms.Select(attrs={'class': 'form-control'}),
			}

from django.urls import path, include
from django.contrib.staticfiles.storage import StaticFilesStorage, staticfiles_storage
from django.views.generic.base import RedirectView
from blog import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('blog', views.BlogPostsPage.as_view(), name='blog'),
    path('add_new_post', views.AddPost.as_view(), name='add_new_post'),
    path('add_new_post_success', views.AddPostSuccess.as_view(), name='add_new_post_success'),
    path('like/<slug:slug>', views.LikePost.as_view(), name='like'),
    path('blog/<slug:slug>', views.BlogPost.as_view(), name='blog-post'),

    # path('URL', views.VIEWS-FORM-CLASS-NAME.as_view(), name='PAGE-NAME'),
    ]
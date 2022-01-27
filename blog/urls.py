from django.urls import path, include
from django.contrib.staticfiles.storage import StaticFilesStorage, staticfiles_storage
from django.views.generic.base import RedirectView
from blog import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('blog', views.BlogPage.as_view(), name='blog'),
    path('like/<slug:slug>', views.LikePost.as_view(), name='like'),
    path('blog/<slug:slug>', views.BlogPost.as_view(), name='blog-post'),

    # path('URL', views.VIEWS-FORM-CLASS-NAME.as_view(), name='PAGE-NAME'),
    ]
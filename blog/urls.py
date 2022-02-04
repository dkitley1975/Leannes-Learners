from django.urls import path, include
from django.contrib.staticfiles.storage import StaticFilesStorage, staticfiles_storage
from django.views.generic.base import RedirectView
from blog import views

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('blog', views.BlogPostsPage.as_view(), name='blog'),    
    path('add_new_post', staff_member_required(login_url='login')(views.AddPost.as_view()), name='add_new_post'),
    path('<slug:slug>', staff_member_required(login_url='login')(views.UpdatePost.as_view()), name='update_post'),
    path('<slug:slug>/remove', staff_member_required(login_url='login')(views.DeletePost.as_view()), name='delete_post'),

    path('add_new_post_success', views.AddPostSuccess.as_view(), name='add_new_post_success'),
    path('like/<slug:slug>', views.LikePost.as_view(), name='like'),
    path('blog/<slug:slug>', views.BlogPost.as_view(), name='blog-post'),

    # path('URL', views.VIEWS-FORM-CLASS-NAME.as_view(), name='PAGE-NAME'),
    ]

from django.urls import path, include
from django.contrib.staticfiles.storage import StaticFilesStorage, staticfiles_storage
from django.views.generic.base import RedirectView
from blog import views

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('posts', views.BlogPostsPage.as_view(), name='blog'),    
    path('create-new-post', staff_member_required(login_url='login')(views.CreatePost.as_view()), name='create-new-post'),
    path('edit/<slug:slug>', staff_member_required(login_url='login')(views.UpdatePost.as_view()), name='update-post'),
    path('<slug:slug>/remove', staff_member_required(login_url='login')(views.DeletePost.as_view()), name='delete-post'),
    path('categories/<category>', views.CategoryListView.as_view(), name='category'),

    path('new-post-successfully_added', views.CreatePostSuccessfull.as_view(), name='add_new_post_success'),
    path('like/<slug:slug>', views.LikePost.as_view(), name='like'),
    path('post/<slug:slug>', views.BlogPost.as_view(), name='blog-post'),
    # path('post/<int:post_pk>/comment/<int:pk>/', views.DeleteComment.as_view(), name='delete-comment'),
    path('post/<slug:slug>/comment/<int:pk>/', views.DeleteComment.as_view(), name='delete-comment'),

    # path('URL', views.VIEWS-FORM-CLASS-NAME.as_view(), name='PAGE-NAME'),
    ]

from django.urls import path, include
from django.contrib.staticfiles.storage import StaticFilesStorage, staticfiles_storage
from django.views.generic.base import RedirectView
from blog import views

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('posts', views.BlogPosts.as_view(), name='blog'),
    path('post-creation', staff_member_required(login_url='login')
        (views.PostCreate.as_view()), name='post-creation'),
    path('<slug:slug>', staff_member_required(login_url='login')
        (views.PostUpdate.as_view()), name='post-update'),
    path('<slug:slug>/remove', staff_member_required(login_url='login')
        (views.PostDelete.as_view()), name='post-delete'),
    path('categories/<category>', views.CategoryList.as_view(), name='category'),
    path('post/<slug:slug>', views.PostDetail.as_view(), name='post-detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='like'),
    path('post/<slug:slug>/comment/<int:pk>/like', views.CommentLike.as_view(),
        name='comment-like'),
    path('post/<slug:slug>/comment/<int:pk>/dislike', views.CommentDislike.as_view(),
        name='comment-dislike'),
    path('post/<slug:slug>/comment/<int:pk>/', views.CommentReply.as_view(),
        name='comment-reply'),
    path('post/<slug:slug>/comment/delete/<int:pk>/', views.CommentDelete.as_view(),
        name='comment-delete'),
    ]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='home'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_post_view'),
    path('blog', views.BlogPage.as_view(), name='blog'),
    path('like/<slug:slug>', views.LikePost.as_view(), name='like'),
    path('accounts/', include('allauth.urls')),
    ]

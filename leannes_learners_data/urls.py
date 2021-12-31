from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='home'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_post_view'),
    path('blog.html', views.BlogPageList.as_view(), name='BlogPageList'),
    path('accounts/', include('allauth.urls')),
    ]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Testimonials.as_view(), name='home'),
    path('blog', views.BlogPage.as_view(), name='blogs'),
    path('pass_plus', views.Passplus.as_view(), name='pass_plus'),
    path('accounts/', include('allauth.urls')),
    path('like/<slug:slug>', views.LikePost.as_view(), name='like'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_post_view'),
    # path('URL', views.VIEWS-FORM-CLASS-NAME.as_view(), name='PAGE-NAME'),
    ]

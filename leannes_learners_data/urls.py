from django.urls import path, include
from django.contrib.staticfiles.storage import StaticFilesStorage, staticfiles_storage
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.Testimonials.as_view(), name='home'),
    path('about-us', views.AboutUsPage.as_view(), name='about-us'),
    path('accounts/', include('allauth.urls')),
    path('blog', views.BlogPage.as_view(), name='blog'),
    path('contact-us', views.ContactUsPage.as_view(), name='contact-us'),
    path('pass-plus', views.PassPlusPage.as_view(), name='pass-plus'),
    path('prices', views.PricesPage.as_view(), name='prices'),
    path('success', views.ContactSuccessView.as_view(), name='success'),
    path('terms-and-conditions', views.TermsPage.as_view(), name='terms-and-conditions'),
    path('like/<slug:slug>', views.LikePost.as_view(), name='like'),
    path('blog/<slug:slug>', views.BlogPost.as_view(), name='blog-post'),

    # path('URL', views.VIEWS-FORM-CLASS-NAME.as_view(), name='PAGE-NAME'),
    ]
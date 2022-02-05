from django.urls import path, include
from django.contrib.staticfiles.storage import StaticFilesStorage, staticfiles_storage
from django.views.generic.base import RedirectView
from leannes_learners_data import views

urlpatterns = [
    path('', views.Testimonials.as_view(), name='home'),
    path('about-us', views.AboutUsPage.as_view(), name='about-us'),
    path('contact-us', views.ContactUsPage.as_view(), name='contact-us'),
    path('pass-plus', views.PassPlusPage.as_view(), name='pass-plus'),
    path('prices', views.PricesPage.as_view(), name='prices'),
    path('success', views.ContactSuccessView.as_view(), name='success'),
    path('terms-and-conditions', views.TermsPage.as_view(), name='terms-and-conditions'),

    # path('URL', views.VIEWS-FORM-CLASS-NAME.as_view(), name='PAGE-NAME'),
    ]

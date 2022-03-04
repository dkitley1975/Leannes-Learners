from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import TemplateView
from leannes_learners_data import views

urlpatterns = [
    path('', views.Testimonials.as_view(), name='home'),
    path('about-us', views.AboutUsPage.as_view(), name='about-us'),
    path('contact-us', views.ContactUsPage.as_view(), name='contact-us'),
    path('pass-plus', views.PassPlusPage.as_view(), name='pass-plus'),
    path('prices', views.PricesPage.as_view(), name='prices'),
    path('success', views.ContactSuccessView.as_view(), name='success.html'),
    path('terms-and-conditions', views.TermsPage.as_view(), name='terms-and-conditions'),
    path('local-traffic', TemplateView.as_view(template_name="pages/local-traffic.html"), name='local-traffic'),

    # path('URL', views.VIEWS-FORM-CLASS-NAME.as_view(), name='PAGE-NAME'),
    ]

from django.urls import path, include
from django.contrib.staticfiles.storage import StaticFilesStorage, staticfiles_storage
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.Testimonials.as_view(), name='home'),
    path('about_us', views.AboutUsPage.as_view(), name='about_us'),
    path('accounts/', include('allauth.urls')),
    path('blog', views.BlogPage.as_view(), name='blogs'),
    path('contact_us', views.ContactUsPage.as_view(), name='contact_us'),
    path('pass_plus', views.PassPlusPage.as_view(), name='pass_plus'),
    path('prices', views.PricesPage.as_view(), name='prices'),
    path('success', views.ContactSuccessView.as_view(), name='success'),
    path('terms_and_conditions', views.TermsPage.as_view(), name='terms_and_conditions'),
    path('like/<slug:slug>', views.LikePost.as_view(), name='like'),
    path('<slug:slug>', views.BlogDetail.as_view(), name='blog_post_view'),

    # path('URL', views.VIEWS-FORM-CLASS-NAME.as_view(), name='PAGE-NAME'),
    ]
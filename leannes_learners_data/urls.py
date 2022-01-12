from django.urls import path, include
from django.contrib.staticfiles.storage import StaticFilesStorage, staticfiles_storage
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.Testimonials.as_view(), name='home'),
    path('contact.html', views.contact, name='contact'),
    path('about_us', views.AboutUsPage.as_view(), name='about_us'),
    path('accounts/', include('allauth.urls')),
    path('blog', views.BlogPage.as_view(), name='blogs'),

    path('pass_plus', views.PassPlusPage.as_view(), name='pass_plus'),
    path('prices', views.PricesPage.as_view(), name='prices'),
    path('like/<slug:slug>', views.LikePost.as_view(), name='like'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_post_view'),
    # path('URL', views.VIEWS-FORM-CLASS-NAME.as_view(), name='PAGE-NAME'),
    # path(
    #     "favicon.ico",
    #     RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    # ),
    # path(
    #     "apple-touch-icon.png",
    #     RedirectView.as_view(url=staticfiles_storage.url("apple-touch-icon.png")),
    # ),
    # path(
    #     "maskable-icon.png",
    #     RedirectView.as_view(url=staticfiles_storage.url("maskable-icon.png")),
    # ),
    # path(
    #     "site.webmanifest",
    #     RedirectView.as_view(url=staticfiles_storage.url("site.webmanifest")),
    # ),
    ]
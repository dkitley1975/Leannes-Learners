"""leannes_learners URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from allauth.account.models import EmailAddress
from django.contrib.sites.models import Site
from django_summernote.utils import get_attachment_model

from leannes_learners import views
from django.conf.urls import handler400, handler404, handler403, handler500


admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(Site)
admin.site.unregister(EmailAddress)
admin.site.unregister(get_attachment_model())

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("django.contrib.auth.urls")),
    path("members/", include("users.urls"), name="users_urls"),
    path("", include("leannes_learners_data.urls"), name="leannes_learners_data_urls"),
    path("blog/", include("blog.urls"), name="blog_urls"),
    path("django_summernote/", include("django_summernote.urls")),
]

handler400 = "leannes_learners.views.bad_request_error_400"
handler403 = "leannes_learners.views.forbidden_error_403"
handler404 = "leannes_learners.views.page_not_found_view_404"
handler500 = "leannes_learners.views.internal_error_500"

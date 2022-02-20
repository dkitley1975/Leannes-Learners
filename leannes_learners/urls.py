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

# Start Unregister from the admin main site panel to help remove confusion for the end user 
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from allauth.account.models import EmailAddress
from django.contrib.sites.models import Site

admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(Site)
admin.site.unregister(EmailAddress)
# end of Unregister from the admin main site panel to help remove confusion for the end user 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('django_summernote/', include('django_summernote.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('leannes_learners_data.urls'), name='leannes_learners_data_urls'),
    path('blog/', include('blog.urls'), name='blog_urls'),
    path('members/', include('users.urls'), name='users_urls'),

]

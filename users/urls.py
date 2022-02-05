from django.urls import path, include
from users import views

urlpatterns = [
    path('register/', views.NewUserRegistrationView.as_view(), name='register'),

    # path('URL', views.VIEWS-FORM-CLASS-NAME.as_view(), name='PAGE-NAME'),
    ]
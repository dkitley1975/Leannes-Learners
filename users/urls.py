from django.urls import path, include
from users import views

urlpatterns = [
    path('password/', views.UpdatePasswordView.as_view(), name='update_password.html'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('edit_profile/', views.UpdateProfileView.as_view(), name='edit_profile'),

    # path('URL', views.VIEWS-FORM-CLASS-NAME.as_view(), name='PAGE-NAME'),
]
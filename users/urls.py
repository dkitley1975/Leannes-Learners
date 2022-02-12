from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required


from users import views

urlpatterns = [
    path('password/', views.UpdatePasswordView.as_view(), name='update-password.html'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('edit-user-details', login_required(views.EditUserDetailsForm.as_view()), name='edit-user-details'),
    path('edit-profile/<int:pk>', login_required(views.EditUserProfile.as_view()), name='edit-profile'),

    # path('URL', views.VIEWS-FORM-CLASS-NAME.as_view(), name='PAGE-NAME'),
]
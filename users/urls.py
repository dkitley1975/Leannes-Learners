from django.urls import path
from django.contrib.auth import views as auth_views
from users import views

urlpatterns = [
    path('password/', views.PasswordUpdateView.as_view(),
         name='change-password'),
    path('password-reset/', auth_views.PasswordResetView.as_view(),
         name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password-reset-done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password-reset-confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password-reset-complete'),
    path('register/', views.UserRegistrationView.as_view(),
         name='register'),
    path('edit-user-details', views.EditUserDetailsForm.as_view(),
         name='edit-user-details'),
    path('edit-profile/<int:pk>', views.EditUserProfile.as_view(),
         name='edit-profile'),
]

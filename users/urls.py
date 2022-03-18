from django.urls import path
from django.contrib.auth import views as auth_views
from users import views

urlpatterns = [
    path('password/', views.PasswordUpdateView.as_view(),
         name='change-password'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    
    path('register/', views.UserRegistrationView.as_view(),
         name='register'),
    
    path('edit-user-details', views.EditUserDetailsForm.as_view(),
         name='edit-user-details'),
    
    path('edit-profile/<int:pk>', views.EditUserProfile.as_view(),
         name='edit-profile'),
]

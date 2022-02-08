from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import UpdateProfileForm, RegistrationForm
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
class UpdatePasswordView(PasswordChangeView):
	form_class = PasswordChangeForm
	template_name = "registration/update_password.html"
	success_url = reverse_lazy('home')
		
	def form_valid(self, form):
		messages.success(self.request, "Your password has been updated successfully.")
		return super().form_valid(form)




class UpdateProfileView(generic.UpdateView):
	form_class = UpdateProfileForm
	template_name = "registration/edit_profile.html"
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user
	
	def form_valid(self, form):
		messages.success(self.request, "Your profile has been updated successfully.")
		return super().form_valid(form)
	
class UserRegistrationView(generic.CreateView):
	form_class = RegistrationForm
	template_name = "registration/register.html"
	success_url = reverse_lazy('login')
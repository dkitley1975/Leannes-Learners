from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import UpdateProfileForm, RegistrationForm
from django.urls import reverse_lazy

# Create your views here.
class UserRegistrationView(generic.CreateView):
	form_class = RegistrationForm
	template_name = "registration/register.html"
	success_url = reverse_lazy('login')

class UpdateProfileView(generic.UpdateView):
	form_class = UpdateProfileForm
	template_name = "registration/edit_profile.html"
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user
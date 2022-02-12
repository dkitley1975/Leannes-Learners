from django.contrib.auth.mixins import LoginRequiredMixin

from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import EditUserDetailsForm, RegistrationForm, EditUserProfileForm
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from .models import UserProfile
from leannes_learners_data.models import CompanyDetails
from django.contrib.auth.mixins import LoginRequiredMixin

	
	

class UserProfileView(DetailView):
	model = UserProfile
	template_name = 'registration/user-profile.html'

def get_context_data(self, *args, **kwargs):
				""" gets the id of a users profile """
				# users = UserProfile.objects.all()
				context = super(UserProfileView, self).get_context_data(*args, **kwargs)
				users_profile_id = get_object_or_404(UserProfile,id=self.kwargs['pk'])
				context['users_profile_id'] = users_profile_id
				return context


# Create your views here.
class UserRegistrationView(generic.CreateView):
	form_class = RegistrationForm
	template_name = "registration/register.html"
	success_url = reverse_lazy('login')


class UpdatePasswordView(PasswordChangeView):
	form_class = PasswordChangeForm
	template_name = "registration/update-password.html"
	success_url = reverse_lazy('home')
		
	def form_valid(self, form):
		messages.success(self.request, "Your password has been updated successfully.")
		return super().form_valid(form)

class EditUserDetailsForm(generic.UpdateView):
	form_class = EditUserDetailsForm
	template_name = "registration/edit-user-details.html"
	success_url = reverse_lazy('edit-user-details')

	def get_object(self):
		return self.request.user

	def form_valid(self, form):
		messages.success(self.request, "Your user details has been updated successfully.")
		return super().form_valid(form)
	
	def get_context_data(self, **kwargs):
		""" Gets the Company Contact info """
		context = super().get_context_data(**kwargs)
		context['social'] = CompanyDetails.objects.all()[0:1]
		return context

class EditUserProfile(LoginRequiredMixin, generic.UpdateView):
	model = UserProfile
	template_name = "registration/edit-profile.html"
	success_url = reverse_lazy('edit-profile')
	form_class = EditUserProfileForm

	def get_success_url(self):
		pk = self.kwargs['pk']
		return reverse_lazy('edit-profile', kwargs={'pk': pk})

	def get_context_data(self, **kwargs):
		""" Gets the Company Contact info """
		context = super().get_context_data(**kwargs)
		context['social'] = CompanyDetails.objects.all()[0:1]
		return context
	
	def form_valid(self, form):
		messages.success(self.request, "Your profile has been updated successfully.")
		return super().form_valid(form)

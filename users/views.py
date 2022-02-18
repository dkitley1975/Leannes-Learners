from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import EditUserDetailsForm, RegistrationForm, EditUserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from .models import UserProfile
# from django.urls import reverse
# from multiprocessing import context
# from django.views.generic import DetailView


# Create your views here.
class UserRegistrationView(generic.CreateView):
	form_class = RegistrationForm
	template_name = "registration/register.html"
	success_url = reverse_lazy('login')


class PasswordUpdateView(PasswordChangeView):
	form_class = PasswordChangeForm
	template_name = "registration/change-password.html"
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		messages.success(self.request, "Your password has been updated successfully.")
		return super().form_valid(form)


class EditUserDetailsForm(LoginRequiredMixin, generic.UpdateView):
	form_class = EditUserDetailsForm
	template_name = "registration/edit-user-details.html"
	success_url = reverse_lazy('edit-user-details')

	def get_object(self):
		return self.request.user

	def form_valid(self, form):
		messages.success(self.request, "Your user details has been updated successfully.")
		return super().form_valid(form)


class EditUserProfile(LoginRequiredMixin, generic.UpdateView):
	model = UserProfile
	template_name = "registration/edit-profile.html"
	success_url = reverse_lazy('edit-profile')
	form_class = EditUserProfileForm

	def get_success_url(self):
		pk = self.kwargs['pk']
		return reverse_lazy('edit-profile', kwargs={'pk': pk})

	def form_valid(self, form):
		messages.success(self.request, "Your profile has been updated successfully.")
		return super().form_valid(form)


# class UserProfileView(LoginRequiredMixin, DetailView):
# 	model = UserProfile
# 	template_name = 'registration/user-profile.html'

# 	def get_context_data(self, *args, **kwargs):
# 		""" gets the id of a users profile """
# 		# users = UserProfile.objects.all()
# 		context = super(UserProfileView, self).get_context_data(*args, **kwargs)
# 		users_profile_id = get_object_or_404(UserProfile,id=self.kwargs['pk'])
# 		context['users_profile_id'] = users_profile_id
# 		return context
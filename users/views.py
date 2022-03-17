from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import EditUserDetailsForm, RegistrationForm, EditUserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from .models import UserProfile


# Create your views here.
class UserRegistrationView(generic.CreateView):
    """
    The registration view for the user.
    This is a generic view that will handle the creation of a new user.
    """
    form_class = RegistrationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class PasswordUpdateView(PasswordChangeView):
    """
    When the form is valid, we want to redirect the user to a success page.
    We can do this by calling the super().form_valid(form) method.
    """
    form_class = PasswordChangeForm
    template_name = "registration/change_password.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        """
        When the form is valid, we want to redirect the user to a success page.
        We can do this by calling the super().form_valid(form) method.
        """
        messages.success(self.request, "Your password has been updated successfully.")
        return super().form_valid(form)


class EditUserDetailsForm(LoginRequiredMixin, generic.UpdateView):
    """
    When the form is valid, we want to redirect the user to the success page.
    We also want to display a success message to the user.
    We override the form_valid method to do this.
    """
    form_class = EditUserDetailsForm
    template_name = "registration/edit-user-details.html"
    success_url = reverse_lazy("edit-user-details")

    def get_object(self):
        """
        Get the current user's object.
        """
        return self.request.user

    def form_valid(self, form):
        """
        When the form is valid,
        we want to redirect the user to the success page. We also want to
        display a success message to the user.
        We override the form_valid method to do this.
        """
        messages.success(
            self.request, "Your user details has been updated successfully."
        )
        return super().form_valid(form)


class EditUserProfile(LoginRequiredMixin, generic.UpdateView):
    """
    When the form is valid, we want to redirect the user to the profile page.
    We also want to display a success message.
    """
    model = UserProfile
    template_name = "registration/edit-profile.html"
    success_url = reverse_lazy("edit-profile")
    form_class = EditUserProfileForm

    def get_success_url(self):
        """
        Get the success url for the profile page.
        """
        pk = self.kwargs["pk"]
        return reverse_lazy("edit-profile", kwargs={"pk": pk})

    def form_valid(self, form):
        """
        When the form is valid,
        we want to redirect the user to the profile page.
        We also want to display a success message.
        """
        messages.success(self.request, "Your profile has been updated successfully.")
        return super().form_valid(form)

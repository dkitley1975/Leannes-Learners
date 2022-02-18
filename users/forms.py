from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from users.models import UserProfile


class RegistrationForm(UserCreationForm):
    """Form to collect registration details"""
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        """declaring the model and fields to use"""
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditUserDetailsForm(UserChangeForm):
    """Form to edit the User Details (name ,email, username)"""
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        """declaring the model and fields to use"""
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            )
        exclude = ('id_password',)


class EditUserProfileForm(UserChangeForm):
    """Form to edit the User Profile Details (Bio and Social)"""
    class Meta:
        """declaring the model and fields to use"""
        model = UserProfile
        fields = (
        'user_bio',
        'user_profile_image',
        'user_facebook_url',
        'user_twitter_url',
        'user_linkedin_url',
        'user_website_url',
            )
        exclude = ('id_password',)

        widgets = {
            'user_bio': forms.Textarea(
                attrs={'class': 'form-control'}),
            'user_facebook_url': forms.TextInput(
                attrs={'class': 'form-control'}),
            'user_twitter_url': forms.TextInput(
                attrs={'class': 'form-control'}),
            'user_linkedin_url': forms.TextInput(
                attrs={'class': 'form-control'}),
            'user_website_url': forms.TextInput(
                attrs={'class': 'form-control'}),
            }

from django import forms
from django.core import validators
from django.contrib.auth.models import User
from identification_app.models import Profile


class LoginForm(forms.Form):
	username = forms.CharField(max_length=150)
	password = forms.CharField(widget=forms.PasswordInput())
	def clean(self):
		all_clean_data = super().clean()
		return all_clean_data


class UserForm(forms.ModelForm):
	password = forms.CharField(widget= forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio', 'profile_pic')

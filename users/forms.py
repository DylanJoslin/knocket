from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class RegistrationForm(UserCreationForm):
    class Meta: 
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'password1', 
            'password2'
        ]

class LoginForm(forms.Form):
    username = forms.CharField(
        label = 'Username',
        max_length = 100
    )
    password = forms.CharField(
        label = 'Password',
        min_length = 8,
        max_length = 50,
        widget=forms.PasswordInput()
    )
    fields = [username, password]
    class Meta:
        model = User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('school',)

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('school',)
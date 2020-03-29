from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

# Model used for registration from the ladning page
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


# Model used along with Registration Form to 
# specify the school the student goes to
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('school',)

class AdminUserProfileForm(forms.ModelForm):
    class Meta: 
        model = UserProfile
        fields = ('school', 'access')


# Model for loging into the website
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


# Model used by the student to update their profile
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]

# Model used by the student in conjunction with UserUpdateForm
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'school',
        )

# Model used by an Administrator/Teacher to update a students info on their behalf
class AdminUserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email'
        ]


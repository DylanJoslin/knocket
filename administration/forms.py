from django import forms
from django.contrib.auth.models import User
from users.models import UserProfile

class AccessForm(forms.ModelForm):
    class Meta: 
        model = UserProfile
        fields = (
            'access',
        )
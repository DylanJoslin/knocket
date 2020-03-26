from django import forms
from django.contrib.auth.models import User
from users.models import UserProfile
from stories.models import VideoPost

class AccessForm(forms.ModelForm):
    class Meta: 
        model = UserProfile
        fields = (
            'access',
        )


class AdminPostForm(forms.ModelForm):

    class Meta:
        model = VideoPost
        fields = ('category','school', 'title', 'slug', 'content', 'video', 'image', 'approve')

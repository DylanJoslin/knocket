from django import forms
from .models import VideoPost

class PostForm(forms.ModelForm):

    class Meta:
        model = VideoPost
        fields = ('category','school', 'title', 'slug', 'content', 'video', 'image',)
        widgets = {'slug': forms.HiddenInput()}

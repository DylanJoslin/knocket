from django.shortcuts import render
from django.views.generic import ListView
from .models import VideoPost

class VideoListView(ListView):
    model = VideoPost
    template_name = 'stories/browse.html'
    context_object_name = 'video_posts'
    ordering = ['-date_posted']
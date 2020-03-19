from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import VideoPost
from .forms import PostForm
from django.shortcuts import redirect
# Create your views here.

def post_list(request):
# def post_list(request, post_category):
    posts = VideoPost.objects.order_by('-date_posted')
    # content = {
    #     'video_posts': VideoPost.objects.all()
    # }
    # return render(request, 'stories/browse.html', context)
    return render(request, 'stories/browse.html', {'posts': posts})

def post_detail(request, post_slug):
    # post = get_object_or_404(VideoPost, pk=pk)
    post = get_object_or_404(VideoPost, slug=post_slug)
    return render(request, 'stories/post_detail.html', {'post': post})

def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return render(request, 'stories/post_detail.html')
        else:
            form = PostForm()
        return render(request, 'stories/post_new.html', {'form': form})
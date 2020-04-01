from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import VideoPost
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def browse(request):
    return render(request, 'stories/browse.html')

def post_list(request):
    school_slug = request.GET.get('school')
    category_slug = request.GET.get('category')

    if VideoPost.objects.filter(school=school_slug).filter(category=category_slug).filter(approve = 1).exists():

        posts = VideoPost.objects.all().filter(approve = 1)
    
        if school_slug:
            posts = posts.filter(school=school_slug)
        
        if category_slug:
            posts = posts.filter(category=category_slug)
    
        posts = posts.order_by('-date_posted')
    
        return render(request, 'stories/post_list.html', {'posts': posts})
    return render(request, 'stories/no_post.html')

def post_detail(request, post_slug):
    post = get_object_or_404(VideoPost, slug=post_slug)
    return render(request, 'stories/post_detail.html', {'post': post})

def post_new(request):
    if not request.user.is_authenticated:
        return redirect('/')
    elif request.user.userprofile.access == 'pending' or request.user.userprofile.access == 'student':
        return redirect('/')
    else:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return render(request, 'users/profile.html')
        else:
            form = PostForm()
        return render(request, 'stories/post_new.html', {'form': form})

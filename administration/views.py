from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from users.forms import AdminUserUpdateForm, AdminUserProfileForm, RegistrationForm, LoginForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from stories.models import VideoPost
from .forms import AdminPostForm
# import pdb;pdb.set_trace()


# Create your views here.

def admin_home(request, access='pending', approve=0): 
    if not request.user.is_authenticated:
        return redirect('/')
    elif request.user.userprofile.access == 'pending' or request.user.userprofile.access == 'student':
        return redirect('/')
    else:
        # Count users to pass into context
        new_users = 0
        registered_users = 0
        for user in User.objects.all():
            if user.userprofile.access == 'pending':
                new_users = new_users + 1
            if user.userprofile.access == 'student':
                registered_users = registered_users + 1

        new_post = 0
        approved_post = 0

        for post in VideoPost.objects.all():
            if post.approve == 0:
                new_post = new_post + 1
            if post.approve == 1:
                approved_post = approved_post + 1

        context = {
            'users': User.objects.all(),
            'new_users': new_users,
            'registered_users': registered_users,
            'access': access,
            'posts': VideoPost.objects.all(),
            'new_post': new_post,
            'approved_post': approved_post,
            'approve': approve
        }


        return render(request, 'administration/admin_home.html', context)


def admin_users(request, access='pending'):
    if not request.user.is_authenticated:
        return redirect('/')
    elif request.user.userprofile.access == 'pending' or request.user.userprofile.access == 'student':
        return redirect('/')
    else:
        # Count users to pass into context
        new_users = 0
        registered_users = 0
        for user in User.objects.all():
            if user.userprofile.access == 'pending':
                new_users = new_users + 1
            if user.userprofile.access == 'student':
                registered_users = registered_users + 1

        context = {
            'users': User.objects.all(),
            'new_users': new_users,
            'registered_users': registered_users,
            'access': access
        }
        return render(request, 'administration/admin_users.html', context)


def admin_uploads(request, approve = 0):
    if not request.user.is_authenticated:
        return redirect('/')
    elif request.user.userprofile.access == 'pending' or request.user.userprofile.access == 'student':
        return redirect('/')
    else:
        # Count users to pass into context
        new_post = 0
        approved_post = 0
        for post in VideoPost.objects.all():
            if post.approve == 0:
                new_post = new_post + 1
            if post.approve == 1:
                approved_post = approved_post + 1

        context = {
            'posts': VideoPost.objects.all(),
            'new_post': new_post,
            'approved_post': approved_post,
            'approve': approve
        }
        return render(request, 'administration/admin_uploads.html', context)

def edit_upload(request, post_slug):
    if not request.user.is_authenticated:
        return redirect('/')
    elif request.user.userprofile.access == 'pending' or request.user.userprofile.access == 'student':
        return redirect('/')
    else:
        post = get_object_or_404(VideoPost, slug=post_slug)
        if request.method == "POST":
            form = AdminPostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('admin_uploads')
        else:
            form = AdminPostForm(instance=post)
        return render(request, 'administration/create_upload.html', {'form': form})

def delete_upload(request, post_slug):
    if not request.user.is_authenticated:
        return redirect('/')
    elif request.user.userprofile.access == 'pending' or request.user.userprofile.access == 'student':
        return redirect('/')
    else:
        post = get_object_or_404(VideoPost, slug=post_slug)
        post.delete()
        return redirect('admin_uploads')


def edit_users(request, username="none"):
    if not request.user.is_authenticated:
        return redirect('/')
    elif request.user.userprofile.access == 'pending' or request.user.userprofile.access == 'student':
        return redirect('/')
    else:
        if request.user.userprofile.access == 'teacher' or request.user.userprofile.access == 'admin':
            if username != 'none':
                user = User.objects.get(username=username)
                user_form = AdminUserUpdateForm(request.POST, instance=user)
                profile_form = UserProfileForm(request.POST, instance=user.userprofile)
                if request.method == 'POST':
                    user = user_form.save()
                    profile = profile_form.save()
                    profile.user = user
                    profile.save()
                    return redirect('/administration')
                else:
                    user_form = AdminUserUpdateForm(instance=user)
                    profile_form = UserProfileForm(instance=user)
                
                context = {
                    'form': user_form,
                    'profile_form': profile_form,
                    'edited_user': user
                }

                return render(request, 'administration/edit_user.html', context)
        return render(request, 'administration/edit_user.html')


def create_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if request.user.userprofile.access == 'admin':
            profile_form = AdminUserProfileForm(request.POST)
        else:
            profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            user.userprofile.access = 'student'
            user.userprofile.save()
            return redirect('admin_users')
    else: 
        form = RegistrationForm()
        profile_form = AdminUserProfileForm()

    context = {
        'form': form,
        'profile_form': profile_form
    }

    return render(request, 'administration/create_user.html', context)



def delete_user(request, username='none'):
    if request.user.userprofile.access == 'teacher' or request.user.userprofile.access == 'admin':
        if username != 'none':
            user = User.objects.get(username=username)
            user.delete()
            messages.success(request, f'This user has been deleted')
            return redirect('/administration')
    else:
        return redirect('/administration')


def approve_user(request, username='none'):
    if request.user.userprofile.access == 'teacher' or request.user.userprofile.access == 'admin':
        if username != 'none':
            user = User.objects.get(username=username)
            user.userprofile.access = 'student'
            user.userprofile.save()
            return redirect('/administration')
        else:
            return redirect('/administration')

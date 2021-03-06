from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from users.forms import AdminUserUpdateForm, AdminUserProfileForm, RegistrationForm, LoginForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm, AdminProfileUpdateForm
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
        teacher_users = 0
        elder_users = 0
        admin_users = 0
        for user in User.objects.all():
            if user.userprofile.access == 'pending':
                new_users = new_users + 1
            if user.userprofile.access == 'student':
                registered_users = registered_users + 1
            if user.userprofile.access == 'teacher':
                teacher_users = teacher_users + 1
            if user.userprofile.access == 'elder':
                elder_users = elder_users + 1
            if user.userprofile.access == 'admin':
                admin_users = admin_users + 1

        access = [
            'pending',
            'student',
            'teacher',
            'elder',
            'admin'
        ]

        accessCounts = {
            'pending': new_users,
            'student': registered_users,
            'teacher': teacher_users,
            'elder': elder_users,
            'admin': admin_users
        }

        

        new_post = 0
        approved_post = 0

        for post in VideoPost.objects.all():
            if post.approve == 0:
                new_post = new_post + 1
            if post.approve == 1:
                approved_post = approved_post + 1

        context = {
            'users': User.objects.all(),
            'accessCounts': accessCounts,
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
        new_users = 0
        registered_users = 0
        teacher_users = 0
        elder_users = 0
        admin_users = 0
        for user in User.objects.all():
            if user.userprofile.access == 'pending':
                new_users = new_users + 1
            if user.userprofile.access == 'student':
                registered_users = registered_users + 1
            if user.userprofile.access == 'teacher':
                teacher_users = teacher_users + 1
            if user.userprofile.access == 'elder':
                elder_users = elder_users + 1
            if user.userprofile.access == 'admin':
                admin_users = admin_users + 1

        access = [
            'pending',
            'student',
            'teacher',
            'elder',
            'admin'
        ]

        accessCounts = {
            'pending': new_users,
            'student': registered_users,
            'teacher': teacher_users,
            'elder': elder_users,
            'admin': admin_users
        }

        context = {
            'users': User.objects.all(),
            'access': access,
            'accessCounts': accessCounts
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
            form = AdminPostForm(request.POST, request.FILES, instance=post)
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
        if request.method == "POST":
            post.delete()
            return redirect('admin_uploads')
        context = {
            "post": post
        }
        return render(request, "administration/confirm_delete.html", context)


def edit_users(request, username="none"):
    if not request.user.is_authenticated:
        return redirect('/')
    elif request.user.userprofile.access == 'pending' or request.user.userprofile.access == 'student':
        return redirect('/')
    elif request.user.userprofile.access == 'teacher' or request.user.userprofile.access == 'admin':
        if username != 'none':
            user = User.objects.get(username=username)
            user_form = AdminUserUpdateForm(request.POST, instance=user)
            if request.user.userprofile.access == 'admin':
                profile_form = AdminProfileUpdateForm(request.POST, instance=user.userprofile)       
            else: 
                profile_form = ProfileUpdateForm(request.POST, instance=user.userprofile)
            if request.method == 'POST':
                if user_form.is_valid() and profile_form.is_valid():
                    user = user_form.save()
                    # Don't commit profile to database yet
                    profile = profile_form.save(commit=False)
                    # Add user details to profile first
                    profile.user = user
                    # THEN save to database
                    profile.save()
                    return redirect('/administration')
            else: 
                user_form = AdminUserUpdateForm( instance=user)
                if request.user.userprofile.access == 'admin':
                    profile_form = AdminProfileUpdateForm(instance=user.userprofile)       
                else: 
                    profile_form = ProfileUpdateForm(instance=user.userprofile)    

            context = {
                'form': user_form,
                'profile_form': profile_form,
                'edited_user': user
            }

            return render(request, 'administration/edit_user.html', context)


def create_user(request):
    if not request.user.is_authenticated:
        return redirect('/')
    elif request.user.userprofile.access == 'pending' or request.user.userprofile.access == 'student':
        return redirect('/')
    elif request.user.userprofile.access == 'teacher' or request.user.userprofile.access == 'admin':
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
                if request.user.userprofile.access == 'teacher':
                    user.userprofile.access = 'student'
                user.userprofile.save()
                return redirect('admin_users')
        else: 
            form = RegistrationForm()
            if request.user.userprofile.access == 'admin':
                profile_form = AdminUserProfileForm()
            else:
                profile_form = UserProfileForm()
        

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

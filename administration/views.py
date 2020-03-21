from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from users.forms import RegistrationForm, UserProfileForm


# Create your views here.

def admin_home(request, access='pending'): 
    # import pdb;pdb.set_trace()

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

    return render(request, 'administration/admin_home.html', context)

def admin_users(request, access='pending'):
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

def admin_uploads(request, access='pending'):
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
    return render(request, 'administration/admin_uploads.html', context)

def edit_users(request):
    return render(request, 'administration/edit_user.html')

def create_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            user.userprofile.access = 'student'
            user.userprofile.save()
            messages.success(request, f'The students account has been created.')
            return redirect('admin_users')
    else: 
        form = RegistrationForm()
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
            messages.success(request, f'This user has been deleted')
            return render(request, 'administration/admin_home.html')
    else:
        messages.error(request, f'You do not have perission to perform this task.')
        return render(request, 'administration/admin_home.html')

def approve_user(request, username='none'):

    if request.user.userprofile.access == 'teacher' or request.user.userprofile.access == 'admin':
        if username != 'none':
            user = User.objects.get(username=username)
            user.userprofile.access = 'student'
            user.userprofile.save()
            messages.success(request, f'This student has been approved!')
            return redirect('admin_home')
        else:
            messages.success(request, f'Cannot approve user!')
            return render(request, 'administration/admin_home.html')

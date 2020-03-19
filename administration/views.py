from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import AccessForm


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

    # if request.method == 'POST':
    #     access_form = AccessForm(request.POST, instance=request.user)
    #     if form.is_valid():
    #         access = access_form.save(commit=false)
    #         # user_access.user

    # return render(request, 'administration/admin_home.html', context)

def admin_users(request):
    return render(request, 'administration/admin_users.html')

def delete_user(request, username='none'):
    if request.user.userprofile.access == 'teacher' or request.user.userprofile.access == 'admin':
        if username != 'none':
            user = User.objects.get(username=username)
            user.delete()
            messages.success(request, f'This user has been deleted')
            return render(request, 'administration/admin_home.html')

def approve_user(request, username='none'):
        if request.user.userprofile.access == 'teacher' or request.user.userprofile.access == 'admin':
            if username != 'none':
                user = User.objects.get(username=username)
                user.userprofile.access == 'student'
                messages.success(request, f'This student has been approved!')
                return render(request, 'administration/admin_home.html')
            else:
                messages.success(request, f'Cannot approve user!')
                return render(request, 'administration/admin_home.html')

def admin_uploads(request):
    return render(request, 'administration/admin_uploads.html')




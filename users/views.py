from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            # Don't commit profile to database yet
            profile = profile_form.save(commit=False)
            # Add user details to profile first
            profile.user = user
            # THEN save to database
            profile.save()
            login(request, user)

            return redirect('profile')
    else: 
        form = RegistrationForm()
        profile_form = UserProfileForm()

    context = {
        'form': form,
        'profile_form': profile_form
    }

    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def edit_profile(request):
    # TO DO: prepopulate forms with user data. SHOULD work with instance=requeset.user, but it doesnt :( )
    user_form = UserUpdateForm(request.POST, instance=request.user)
    profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
    if request.method == 'POST':
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            # Don't commit profile to database yet
            profile = profile_form.save(commit=False)
            # Add user details to profile first
            profile.user = user
            # THEN save to database
            profile.save()
            return redirect('profile')
    else: 
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = { 
        'form': user_form, 
        'profile_form': profile_form
    }

    return render(request, 'users/edit_profile.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, f'Your login info is invalid. Please try again.')
    else: 
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')


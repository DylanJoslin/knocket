from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import AccessForm


# Create your views here.

def admin_home(request, access='pending'): 
    # import pdb;pdb.set_trace()
    context = {
        'users': User.objects.all(),
        'access': access
    }
    
    return render(request, 'administration/admin_home.html', context)

    if request.method == 'POST':
        access_form = AccessForm(request.POST, instance=request.user)
        if form.is_valid():
            access = access_form.save(commit=false)
            # user_access.user

    return render(request, 'administration/admin_home.html', context)

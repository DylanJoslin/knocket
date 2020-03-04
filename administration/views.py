from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.

def admin_home(request, access='new'): 

    context = {
        'users': User.objects.all(),
        'access': access
    }


    return render(request, 'administration/admin_home.html', context)
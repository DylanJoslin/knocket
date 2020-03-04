from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.

def admin_home(request): 

    context = {
        'users': User.objects.all()
    }

    return render(request, 'administration/admin_home.html', context)
from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.

def admin_home(request, access='new'): 

    context = {
        'users': User.objects.all()
    }

    if request.path == '/administration/new':
        context['access'] = 'pending'
            
    if request.path == '/administration/student':
        context['access'] = 'student'

    if request.path == '/administration/teacher':
        context['access'] = 'teacher'

    if request.path == '/administration/elder':
        context['access'] = 'elder'


    return render(request, 'administration/admin_home.html', context)
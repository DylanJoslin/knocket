from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def home(request):
    return render(request, 'home/map.html')

def resources(request):
    return render(request, 'home/resources.html')

def events(request):
    return render(request, 'home/events.html')

def about(request):
    return render(request, 'home/about.html')

# Each link on the map provides a slug that is passed into the view, and the view determines which html template to load.
# Django doesn't support switch statements, so I used else if
def ProvinceView(request, province_name):
    if province_name == 'ab':
        url = 'home/local-alberta.html'
    elif province_name == 'bc':
        url = 'home/local-bc.html'
    elif province_name == 'sk':
        url = 'home/local-sask.html'
    elif province_name == 'mb':
        url = 'home/local-manitoba.html'
    
    return render(request, url)
        


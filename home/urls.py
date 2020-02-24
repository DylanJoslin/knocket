from django.urls import path
from . import views
from .views import ProvinceView

urlpatterns = [
    path('', views.home, name='home'),
    path('resources/', views.resources, name="resources"),
    path('events/', views.events, name="events"),
    path('about/', views.about, name="about"),
    path('province/<slug:province_name>/', views.ProvinceView, name="province")
]
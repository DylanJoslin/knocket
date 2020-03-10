"""storytelling_prototype URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views
from users import views as user_views
from administration import views as administration_views
from stories import views as story_views
from stories.views import VideoListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('administration/', administration_views.admin_home, name='administration'),
    path('administration/users/', administration_views.admin_users, name='admin_users'),
    path('administration/uploads/', administration_views.admin_uploads, name='admin_uploads'),
    path('administration/edit-user/', administration_views.edit_users, name='edit_users'),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('stories/', story_views.stories, name='stories'),
    path('stories/<slug:school>/', VideoListView.as_view(), name='stories'),
    path('profile/', user_views.profile, name="profile"),
    path('profile/edit/', user_views.edit_profile, name="edit_profile"),
]

# Changes the pathing for static files while we're in debug mode (which we currently are)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('health', views.all_health_view, name = 'health'),
    path('update', views.update_health_view, name = 'update_health'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name='signup'),
    path('logout', views.logout_view, name='logout'),
    path('', views.home, name='home')
]

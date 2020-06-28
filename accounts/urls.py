from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
]

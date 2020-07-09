from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('register_form', views.register_form, name="register-form"),
    path('logout', views.logout, name="logout"),
]

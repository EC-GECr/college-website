from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('institute', views.institute, name='institute'),
    path('department', views.department, name='department'),
    path('contact', views.contact, name='contact'),
]

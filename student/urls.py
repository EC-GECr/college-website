from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='student-dashboard'),

    path('session', views.session, name="student-session"),
    path('material', views.material, name="student-material"),
    path('industry', views.industry, name="student-industry"),
    path('academic', views.academic, name="student-academic"),
    path('grow', views.grow, name="student-grow"),
    path('feedback', views.feedback, name="student-feedback"),
]

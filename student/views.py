from django.shortcuts import render, redirect


def dashboard(request):
    return render(request, 'student/dashboard.html')


def session(request):
    return render(request, 'student/session.html')


def material(request):
    return render(request, 'student/material.html')


def industry(request):
    return render(request, 'student/industry.html')


def academic(request):
    return render(request, 'student/academic.html')


def grow(request):
    return render(request, 'student/grow.html')


def feedback(request):
    return render(request, 'student/feedback.html')

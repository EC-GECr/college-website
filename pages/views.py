from django.shortcuts import render, redirect


def index(request):
    return render(request, 'pages/index.html')


def institute(request):
    return render(request, 'pages/institute.html')


def department(request):
    return render(request, 'pages/department.html')


def contact(request):
    return render(request, 'pages/contact.html')

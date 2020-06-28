from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            msg = 'Welcome, {}. Create a deck or flip the existing ones!'.format(username)
            messages.success(request, msg)
            return redirect('/flashcard/decks')

        else:
            msg = "Argh! Invalid Credentials"
            messages.error(request, msg)
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def register(request):
    return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
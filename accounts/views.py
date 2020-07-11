from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from student.models import Student


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            # msg = 'Welcome, {}. Create a deck or flip the existing ones!'.format(username)
            # messages.success(request, msg)
            return redirect('/student/dashboard')

        else:
            msg = "Argh! Invalid Credentials"
            messages.error(request, msg)
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def register(request):
    return render(request, 'accounts/register.html')


def register_form(request):
    if request.method == 'POST':

        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['Email']
        phone = request.POST['Phone']
        roll = request.POST['Roll']
        enroll = request.POST['Enroll']

        board1 = request.POST['Board10']
        tenthroll = request.POST['Tenthroll']
        tenthcent = request.POST['Tenthcent']
        board2 = request.POST['Board12']
        twelthroll = request.POST['Twelthroll']
        twelthcent = request.POST['Twelthcent']
        petroll = request.POST['PETroll']
        petrank = request.POST['PETrank']

        fatherfirst = request.POST['FatherFirst']
        fatherlast = request.POST['FatherLast']
        fatherjob = request.POST['FatherJob']
        fatherphone = request.POST['FatherPhone']
        motherfirst = request.POST['MotherFirst']
        motherlast = request.POST['MotherLast']
        motherjob = request.POST['MotherJob']
        motherphone = request.POST['MotherPhone']

        dob = request.POST['dob']
        sex = request.POST['sex']
        blood = request.POST['blood']
        height = request.POST['height']
        weight = request.POST['weight']
        aadhar = request.POST['aadhar']

        student = Student(
            fi
        )

    return render(request, 'accounts/register_form.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')

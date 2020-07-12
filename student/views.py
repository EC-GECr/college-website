from django.shortcuts import render, redirect
from datetime import datetime
from student.models import Student


def get_session_details(grad_year):

    grad_year = int(grad_year)
    current_month = int(datetime.now().strftime('%m'))
    current_year = int(datetime.now().strftime('%Y'))

    current_session = 'Summer'
    semester = 0  # 0 for Even & 1 for Odd

    if current_month > 6:
        current_session = 'Winter'
        semester = 1

    current_semester = 3

    diff = grad_year - current_year
    if diff == 4:
        current_semester = 1
    elif diff == 3:
        if semester == 0:
            current_semester = 2
        else:
            current_semester = 3
    elif diff == 2:
        if semester == 0:
            current_semester = 4
        else:
            current_semester = 5
    elif diff == 1:
        if semester == 0:
            current_semester = 6
        else:
            current_semester = 7
    elif diff == 0:
        current_semester = 8

    else:
        current_semester = -1

    return current_semester, current_session


def get_info(request):
    user_id = request.user.id
    student = Student.objects.get(pk=user_id)

    first_name = student.first_name
    last_name = student.last_name
    email = student.email

    name = f'{first_name} {last_name}'
    grad_year = student.grad_year
    current_semester, current_session = get_session_details(grad_year)

    return name, email, current_session, current_semester


def dashboard(request):
    return render(request, 'student/dashboard.html')


def session(request):
    name, email, current_session, current_semester = get_info(request)
    current_year = int(datetime.now().strftime('%Y'))
    ctx = {
        'name': name,
        'email': email,
        'current_session': current_session,
        'current_semester': current_semester,
        'current_year': current_year
    }
    return render(request, 'student/session.html', ctx)


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

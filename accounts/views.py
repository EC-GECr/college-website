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
            return redirect('/student/dashboard')

        else:
            msg = "Argh! Invalid Credentials"
            messages.error(request, msg)
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def register(request):
    return render(request, 'accounts/register.html')


def register_account(request):

    if request.method == 'POST':

        # Get Form Values
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check: Match Passwords
        if password1 == password2:

            # Check: Username Availability
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username {name} is already taken'.format(name=username))
                return redirect('register-account')

            user = User.objects.create_user(username=username, password=password1)
            user.save()
            auth.login(request, user)

            return render(request, 'accounts/register_form.html')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register-account')

    return render(request, 'accounts/register_account.html')


def register_form(request):

    if request.method == 'POST':
        user_id = request.user.id
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['Email']
        phone = request.POST['Phone']
        roll = request.POST['Roll']
        enroll = request.POST['Enroll']
        grad_year = request.POST['GradYear']

        board1 = request.POST['Board10']
        tenthroll = request.POST['TenthRoll']
        tenthcent = request.POST['TenthCent']
        board2 = request.POST['Board12']
        twelthroll = request.POST['TwelthRoll']
        twelthcent = request.POST['TwelthCent']
        petroll = request.POST['PETRoll']
        petrank = request.POST['PETRank']

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
            user_id=user_id,
            is_student=True,
            is_faculty=False,

            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            roll_number=roll,
            enroll_number=enroll,
            grad_year=grad_year,

            tenth_board=board1,
            tenth_roll_number=tenthroll,
            tenth_cent=tenthcent,
            twelfth_board=board2,
            twelfth_roll_number=twelthroll,
            twelfth_cent=twelthcent,
            pet_roll_number=petroll,
            pet_rank=petrank,

            father_first=fatherfirst,
            father_last=fatherlast,
            father_phone=fatherphone,
            father_job=fatherjob,
            mother_first=motherfirst,
            mother_last=motherlast,
            mother_phone=motherphone,
            mother_job=motherjob,

            dob=dob,
            gender=sex,
            blood_group=blood,
            height=height,
            weight=weight,
            aadhar_number=aadhar
        )
        student.save()
        auth.logout(request)
        return render(request, 'accounts/register_success.html')

    return render(request, 'accounts/register_form.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')

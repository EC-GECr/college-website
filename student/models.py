from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    is_student = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=True)

    # Tell us about yourself
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    roll_number = models.CharField(max_length=20, unique=True)
    username = None
    enroll_number = models.CharField(max_length=20)

    # Academic Details
    tenth_board = models.IntegerField()
    tenth_roll_number = models.CharField(max_length=50)
    tenth_cent = models.CharField(max_length=10)

    twelfth_board = models.IntegerField()
    twelfth_roll_number = models.CharField(max_length=50)
    twelfth_cent = models.CharField(max_length=10)

    pet_roll_number = models.CharField(max_length=30)
    pet_rank = models.CharField(max_length=8)

    # Family details
    father_first = models.CharField(max_length=30)
    father_last = models.CharField(max_length=30)
    father_job = models.CharField(max_length=30)
    father_phone = models.CharField(max_length=30)

    mother_first = models.CharField(max_length=30)
    mother_last = models.CharField(max_length=30)
    mother_job = models.CharField(max_length=30)
    mother_phone = models.CharField(max_length=30)

    # Personal Info
    dob = models.DateField()
    gender = models.IntegerField()
    blood_group = models.CharField(max_length=5)
    height = models.IntegerField()
    weight = models.IntegerField()
    aadhar_number = models.CharField(max_length=30)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

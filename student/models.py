from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    is_student = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=True)

    # Tell us about yourself
    first_name = models.CharField(max_length=30, default='NA')
    last_name = models.CharField(max_length=30, default='NA')
    email = models.CharField(max_length=50, default='NA')
    phone = models.CharField(max_length=20, default='NA')
    roll_number = models.CharField(max_length=20, default='NA')
    enroll_number = models.CharField(max_length=20, default='NA')
    grad_year = models.CharField(max_length=20, default='NA')

    # Academic Details
    tenth_board = models.CharField(max_length=100, default='NA')
    tenth_roll_number = models.CharField(max_length=50, default='NA')
    tenth_cent = models.CharField(max_length=20, default='NA')

    twelfth_board = models.CharField(max_length=100, default='NA')
    twelfth_roll_number = models.CharField(max_length=50, default='NA')
    twelfth_cent = models.CharField(max_length=20, default='NA')

    pet_roll_number = models.CharField(max_length=30, default='NA')
    pet_rank = models.CharField(max_length=20, default='NA')

    # Family details
    father_first = models.CharField(max_length=30, default='NA')
    father_last = models.CharField(max_length=30, default='NA')
    father_job = models.CharField(max_length=30, default='NA')
    father_phone = models.CharField(max_length=30, default='NA')

    mother_first = models.CharField(max_length=30, default='NA')
    mother_last = models.CharField(max_length=30, default='NA')
    mother_job = models.CharField(max_length=30, default='NA')
    mother_phone = models.CharField(max_length=30, default='NA')

    # Personal Info
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=20, default='NA')
    blood_group = models.CharField(max_length=5, default='NA')
    height = models.IntegerField(default=-1)
    weight = models.IntegerField(default=-1)
    aadhar_number = models.CharField(max_length=30, default='NA')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()

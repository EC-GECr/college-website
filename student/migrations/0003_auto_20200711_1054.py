# Generated by Django 3.0.7 on 2020-07-11 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200711_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='aadhar_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='blood_group',
        ),
        migrations.RemoveField(
            model_name='student',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='enroll_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='father_first',
        ),
        migrations.RemoveField(
            model_name='student',
            name='father_job',
        ),
        migrations.RemoveField(
            model_name='student',
            name='father_last',
        ),
        migrations.RemoveField(
            model_name='student',
            name='father_phone',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='student',
            name='height',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_faculty',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='mother_first',
        ),
        migrations.RemoveField(
            model_name='student',
            name='mother_job',
        ),
        migrations.RemoveField(
            model_name='student',
            name='mother_last',
        ),
        migrations.RemoveField(
            model_name='student',
            name='mother_phone',
        ),
        migrations.RemoveField(
            model_name='student',
            name='pet_rank',
        ),
        migrations.RemoveField(
            model_name='student',
            name='pet_roll_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='student',
            name='roll_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='tenth_board',
        ),
        migrations.RemoveField(
            model_name='student',
            name='tenth_cent',
        ),
        migrations.RemoveField(
            model_name='student',
            name='tenth_roll_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='twelfth_board',
        ),
        migrations.RemoveField(
            model_name='student',
            name='twelfth_cent',
        ),
        migrations.RemoveField(
            model_name='student',
            name='twelfth_roll_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='weight',
        ),
    ]

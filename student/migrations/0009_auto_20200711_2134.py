# Generated by Django 3.0.7 on 2020-07-11 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20200711_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(default='NA', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='pet_rank',
            field=models.CharField(default='NA', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(default='NA', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='tenth_board',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='tenth_cent',
            field=models.CharField(default='NA', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelfth_board',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelfth_cent',
            field=models.CharField(default='NA', max_length=20),
        ),
    ]

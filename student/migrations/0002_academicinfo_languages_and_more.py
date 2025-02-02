# Generated by Django 5.0.2 on 2024-04-30 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicinfo',
            name='languages',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='academicinfo',
            name='project_description',
            field=models.TextField(default='Default Project Description'),
        ),
        migrations.AddField(
            model_name='academicinfo',
            name='skills',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]

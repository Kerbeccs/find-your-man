# Generated by Django 5.0.2 on 2024-05-01 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_academicinfo_languages_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='languages',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='project_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='skills',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]

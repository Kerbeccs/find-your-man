from django.db import models
from django.contrib.auth.models import User, AbstractUser

    

class Profile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    student_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10,  choices=GENDER_CHOICES)
    registration_number = models.CharField(max_length=20, unique=True,primary_key="")
    batch = models.IntegerField()
    branch = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    birthday = models.DateField()
    
    def __str__(self):
        return self.student_name

class Branch(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

from django.db import models
from .models import Profile

class Achievement(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    academic_achievements = models.TextField()
    academic_certificate = models.FileField(upload_to='achievement_certificates/')
    extracurricular_activities = models.TextField()
    eca_achievements = models.FileField(upload_to='achievement_certificates/')

    def __str__(self):
        return f"{self.profile.student_name}'s Achievements"

from django.db import models
from .models import Profile

class AcademicInfo(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    cgpa = models.DecimalField(max_digits=5, decimal_places=2)
    current_year = models.IntegerField()
    tenth_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    twelfth_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    leetcode_profile = models.URLField(max_length=200)
    linkedin_profile = models.URLField(max_length=200)
    github_profile = models.URLField(max_length=200)
    hackerrank_profile = models.URLField(max_length=200)
    languages = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    project_description = models.TextField(null=True)
    def __str__(self):
        return f"{self.profile.student_name}'s Academic Info"
 
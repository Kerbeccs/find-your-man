from django.urls import path
from . import views

# urls.py (inside your Django app)



urlpatterns = [
    path('login/', views.StudentLoginView.as_view(), name='login'),
    path('profile/', views.stud1, name='stw' ),
    path('academicinfo/', views.stud2, name='2' ),
    path('achievement/', views.stud3, name='3' ),
    path('noti/', views.stud4, name='4' ),
    path('academicinfo/', views.insert_academic_info, name='academicinfo'),
    path('', views.profile, name='profile'),
]

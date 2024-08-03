from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    path('login/', views.TeacherLoginView.as_view(), name='login'),
    # Add other URLs for teacher app here if needed
    path( 'teach1/', views.teach1, name='teach1'),
    path( 'teach2/', views.teach2, name='teach2'),
]


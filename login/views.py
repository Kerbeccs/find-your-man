from django.shortcuts import render
from django.http import HttpResponse

from student.models import  Profile

# Create your views here.
def index (request):

 return render(request, 'login.html') 
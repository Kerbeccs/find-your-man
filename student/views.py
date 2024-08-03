from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Profile
class StudentLoginView(FormView):
    template_name = 'student/login.html'
    form_class = AuthenticationForm
    success_url = '/'  

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

def stud1 (request):
    return render (request, 'profile.html')
    
def stud3 (request):
    return render (request, 'achievement.html')
def stud2 (request):
    return render (request, 'academicinfo.html')
def stud4 (request):
    return render (request, 'noti.html')    




from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import JsonResponse
from .models import Profile, AcademicInfo, Achievement
from .forms import AcademicInfoForm, AchievementForm  
from. forms import  ProfileForm


from django.shortcuts import render
from django.http import JsonResponse
from .forms import ProfileForm
from .models import Profile

def profile(request):
    # Initialize an empty form instance by default
    form = ProfileForm()

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = ProfileForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # Process the data in form.cleaned_data to save to the database:
            student_name = form.cleaned_data['student_name']
            gender = form.cleaned_data['gender']
            registration_number = form.cleaned_data['registration_number']
            batch = form.cleaned_data['batch']
            branch = form.cleaned_data['branch']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            birthday = form.cleaned_data['birthday']

            # Save the form data to the database (create a new Profile instance):
            profile = Profile(
                student_name=student_name,
                gender=gender,
                registration_number=registration_number,
                batch=batch,
                branch=branch,
                email=email,
                phone_number=phone_number,
                birthday=birthday
            )
            profile.save()

            # Return a success JSON response (HTTP status 200 OK)
            return JsonResponse({'success': 'Profile information saved successfully!'})

        else:
            # Return a JSON response indicating invalid data (HTTP status 400 Bad Request)
           print(form.errors)

    # Render the form template with the form object:
    return render(request, 'profile_form.html', {'form': form})

from django.shortcuts import render
from django.http import JsonResponse
from .models import AcademicInfo, Achievement, Profile

def insert_academic_info(request):

    page = 'academicinfo'
    form = AcademicInfo()

    if request.method == 'POST':
        
        
        
        cgpa = request.POST.get('cgpa')
        current_year = request.POST.get('current_year')
        tenth_percentage = request.POST.get('tenth_percentage')
        twelfth_percentage = request.POST.get('twelfth_percentage')
        leetcode_profile = request.POST.get('leetcode_profile')
        linkedin_profile = request.POST.get('linkedin_profile')
        github_profile = request.POST.get('github_profile')
        hackerrank_profile = request.POST.get('hackerrank_profile')
        languages = request.POST.get('languages')
        skills = request.POST.get('skills') 
        if (cgpa and current_year and tenth_percentage and
                twelfth_percentage and leetcode_profile and linkedin_profile and
                github_profile and hackerrank_profile and languages):
            
           
            

           
            academic_info = AcademicInfo(
                
                cgpa=float(cgpa),
                current_year=int(current_year),
                tenth_percentage=float(tenth_percentage),
                twelfth_percentage=float(twelfth_percentage),
                leetcode_profile=leetcode_profile,
                linkedin_profile=linkedin_profile,
                github_profile=github_profile,
                hackerrank_profile=hackerrank_profile,
                languages=languages,
                skills=skills  
            )

           
            academic_info.save()

            return JsonResponse({'success': 'Academic information inserted successfully!'})
        else:
              print(form.errors)

    return JsonResponse({'error': 'Invalid request'}, status=400)


def insert_achievement(request):
    if request.method == 'POST' and request.is_ajax():
        profile_id = request.POST.get('profile_id')
        academic_achievements = request.POST.get('academic_achievements')
        academic_certificate = request.FILES.get('academic_certificate')
        extracurricular_activities = request.POST.get('extracurricular_activities')
        eca_achievements = request.FILES.get('eca_achievements')

       
        if (profile_id and academic_achievements and academic_certificate and
                extracurricular_activities and eca_achievements):
            
          
            try:
                profile = Profile.objects.get(id=profile_id)
            except Profile.DoesNotExist:
                return JsonResponse({'error': 'Profile not found'}, status=400)

           
            achievement = Achievement(
                profile=profile,
                academic_achievements=academic_achievements,
                academic_certificate=academic_certificate,
                extracurricular_activities=extracurricular_activities,
                eca_achievements=eca_achievements
            )

          
            achievement.save()

            return JsonResponse({'success': 'Achievement inserted successfully!'})
        else:
             print(form.errors)

    return JsonResponse({'error': 'Invalid request'}, status=400)

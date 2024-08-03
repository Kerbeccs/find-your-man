from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

class TeacherLoginView(FormView):
    template_name = 'teacher/login.html'
    form_class = AuthenticationForm
    success_url = '/'  # Redirect to home page after successful login

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)
def teach1 (request):
        return render (request, 'teach1.html')
def teach2 (request):
        return render (request, 'teach2.html')
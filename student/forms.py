from django import forms
from .models import Profile, Branch, AcademicInfo, Achievement

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'  # Use all fields from the Profile model


class AcademicInfoForm(forms.ModelForm):
    class Meta:
        model = AcademicInfo
        exclude = ('profile',)  # Exclude the 'profile' field from the form (auto-populated)

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        exclude = ('profile',)  # Exclude the 'profile' field from the form (auto-populated)


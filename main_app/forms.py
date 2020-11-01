from django import forms
from .models import Profile

class ProfileCreationForm(form.ModelForm):
    class Meta:
        model = Profile
        fields = ['currentcity', 'picture']
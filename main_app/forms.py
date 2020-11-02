from django import forms
from .models import Profile, Post

class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'firstname', 'lastname', 'currentcity', 'picture' ]

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'date', 'city', 'content', ]
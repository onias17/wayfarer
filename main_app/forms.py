from django import forms
from .models import Profile, Post, City
from django.contrib import admin

class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'firstname', 'lastname', 'currentcity', 'picture' ]

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')



class CityCreationForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'picture', 'country']






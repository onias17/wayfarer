from django import forms
from .models import Profile, Post, City
from smart_selects.db_fields import ChainedForeignKey
from django.contrib import admin
from django_cascading_dropdown_widget.widgets import DjangoCascadingDropdownWidget
from django_cascading_dropdown_widget.widgets import CascadingModelchoices
class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'firstname', 'lastname', 'currentcity', 'picture' ]

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'city', 'content')

    

class CityCreationForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'picture', 'country']






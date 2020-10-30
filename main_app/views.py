from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def profiles_index(request):
    return render(request, 'profiles/index.html')

def signup(request):
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form' : form})

def profiles_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    context = {'profile' : profile}

    return render(request, 'profiles/detail.html', context )

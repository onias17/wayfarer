from django.shortcuts import render, redirect
from . models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def home(request):
    return render(request, 'home.html')

def profiles_index(request):
    return render(request, 'profiles/index.html')

def profiles_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    context = {'profile' : profile}

    return render(request, 'profiles/detail.html', context )

def signup(request):
    error_message = ''

## Handling POST request to signup
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profiles_index')
        else:
            error_message = 'Invalid sign up - please try again'
            form = UserCreationForm()
            context = {'form' : form, 'error_message' : error_message}
            return render(request, 'registration/signup.html', context)
    
## Handling GET request to signup
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
    
    return render(request, 'registration/signup.html', {'form' : form})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ProfileCreationForm, PostCreationForm
from .models import Profile, Post
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

def profiles_index(request):
    return render(request, 'profiles/index.html')

def new_profile(request):
    if request.method == "POST":
        profile_form = ProfileCreationForm(request.POST)
        if profile_form.is_valid():
            new_profile = profile_form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()

            return redirect('detail', new_profile.id)
    else:
        profile_form = ProfileCreationForm()
        context = {'profile_form' : profile_form}
        return render(request, 'profiles/new.html', context)

def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('new_profile')
        else:
            error_message = "Invalid sign up - try again"
            form = UserCreationForm()
            context = {'form': form, 'error_message': error_message}
            return render(request, 'registration/signup.html', context)

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def profiles_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    context = {'profile' : profile}

    return render(request, 'profiles/detail.html', context )


def profiles_edit(request, profile_id):
    profile = Profile.objects.get(id=profile_id)

    if request.method == "POST":
        profile_form = ProfileCreationForm(request.POST, instance=profile)
        if profile_form.is_valid():
            updated_profile = profile_form.save()
            return redirect('detail', updated_profile.id)
    else:
        profile_form  = ProfileCreationForm(instance=profile)
        context = {'profileform': profile_form, 'profile' : profile}
        return render(request, 'profiles/edit.html', context)

def add_post(request, profile_id):
    if request.method == "POST":
        form = PostCreationForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.profile_id = profile_id
            new_form.save()

        return redirect('detail', profile_id)
    else:
        form = PostCreationForm()
        return render(request, 'posts/new.html', {'form': form, 'profile_id' : profile_id})


def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)
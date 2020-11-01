from . import views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', views.home, name="home"),
    path('profiles/index/', views.profiles_index, name="profiles_index"),
    path('profiles/new/', views.new_profile, name="new_profile"),
    path('profiles/<int:profile_id>/', views.profiles_detail, name="detail"),


    path('accounts/signup', views.signup, name='signup')

]

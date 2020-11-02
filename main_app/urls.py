from . import views
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('profiles/index/', views.profiles_index, name="profiles_index"),
    path('profiles/new/', views.new_profile, name="new_profile"),
    path('profiles/<int:profile_id>/', views.profiles_detail, name="detail"),
    path('profiles/<int:profile_id>/edit/', views.profiles_edit, name="edit"),
    path('profiles/<int:profile_id>/add_post/', views.add_post, name="add_post"),

    path('posts/<int:post_id>/', views.posts_detail, name ="postdetail"),

    path('accounts/signup', views.signup, name='signup')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from . import views
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),

    ## PROFILE URLS
    path('profiles/index/', views.profiles_index, name="profiles_index"),
    path('profiles/new/', views.new_profile, name="new_profile"),
    path('profiles/<int:profile_id>/', views.profiles_detail, name="detail"),
    path('profiles/<int:profile_id>/edit/', views.profiles_edit, name="edit"),

    ##POST URLS
    path('profiles/<int:profile_id>/add_post/', views.add_post, name="add_post"),
    path('posts/<int:post_id>/', views.posts_detail, name ="postdetail"),
    path('posts/<int:post_id>/edit', views.post_edit, name="postedit"),
    path('posts/<int:post_id>/delete', views.post_delete, name="deletepost"),

    ##CITY URLS
    path('cities/new', views.add_city, name="add_city"),
    path('cities/index', views.city_index, name="city_index"),
    path('cities/<int:city_id>/', views.city_detail, name="citydetail"),
    ##SIGN UP URL
    path('accounts/signup', views.signup, name='signup'),

    ##EMAIL PATH
    path('success', views.success, name = 'success')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

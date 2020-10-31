from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name="home"),
    path('profiles/index/', views.profiles_index, name="profiles_index"),
    # path('profiles/<int:profile_id>/', views.profiles_detail, name="detail"),


    path('accounts/signup', views.signup, name='signup')

]

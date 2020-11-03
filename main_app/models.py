from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="images/", default='/images/default-profile-img.png')
    currentcity = models.CharField(max_length=100)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length = 50)

    def __str__(self):
        return self.user.username


class City(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="images/", blank = True)
    country = models.CharField(max_length=50)

def __str__(self):
    return self.name


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    title = models.CharField(max_length= 100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)






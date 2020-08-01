from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.user.username




class Photo(models.Model):
    user = models.ForeignKey(User, related_name='photos', on_delete=models.CASCADE)
    site = models.URLField(blank=True, null=True)
    pic = models.ImageField(upload_to='profile_pics',blank=True)
    pic_Number = models.PositiveIntegerField(blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.site
    
    def get_absolute_url(self):
        return reverse('basic_app:photo_list')
    






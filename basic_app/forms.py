from django import forms
from django.contrib.auth.models import User
from .models import Photo



class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')





class PhotoForm(forms.ModelForm):

    class Meta():
        model = Photo
        fields = '__all__'
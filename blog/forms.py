from django import forms
from .models import *
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        
class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','content','image']

class CommentForm(forms.ModelForm):
    # add new field to the form named id
    class Meta:
        model=Comment
        fields=['comment']    
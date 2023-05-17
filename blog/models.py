from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    image=models.ImageField(upload_to="blog/images",default="")

class Comment(models.Model):
    comment=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    comments=models.ManyToManyField('self',blank=True)
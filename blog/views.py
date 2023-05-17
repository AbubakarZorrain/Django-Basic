# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
import json
from . models import *
from . forms import *
def home(request):
    return HttpResponse("Hello, World. You're at the blog's home Page.")

def signup(request):
    if request.method == 'GET':
        signupForm = UserForm()
        return render(request, 'signup.html', {'signupForm': signupForm})

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create(username=username, email=email, password=password)
        if user is not None:
            return HttpResponse("user created successfuly.")

        return HttpResponse("Sorry user not created.", user)

def signin(request):
    if request.method == 'GET':
        loginForm = LoginForm()
        return render(request, 'signin.html', {'loginForm': loginForm})

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate( username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("user logged in successfuly.", user)

        return HttpResponse("user not found.", user)

def create_post(request):
    if request.method == 'GET':
        blogForm = BlogForm()
        return render(request, 'create_post.html', {'postForm': blogForm})

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.POST['image']
        author= request.user
    blog = Blog.objects.create(title=title, content=content, image=image, author=author)
    return HttpResponse("Hello, World. You're at the blog's createPost Page.", blog)

def get_all_posts(request):
    posts = Blog.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def get_post_by_id(request,id):
    commentForm = CommentForm()
    post = Blog.objects.get(id=id)
    comments = Comment.objects.filter(blog=post)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'commentForm': commentForm})
    
def comment(request, id):
    if request.method == 'POST':
        comment = request.POST['comment']
        author= request.user
        blog = Blog.objects.get(id=id)
    comment = Comment.objects.create(comment=comment, blog=blog, author=author)
    return HttpResponse("Hello, World. You're at the blog's comment Page.", comment)
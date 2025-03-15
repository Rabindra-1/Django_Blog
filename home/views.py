from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import posts
from. import models
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def app(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        user = authenticate(request, username=name , password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request,'Invalid Password')
            return redirect('login')   
    return render(request,'home/login.html')

def sign(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        newUser = User.objects.create_user(username=name, email=email, password=password)
        newUser.save()
        return redirect('login')
    return render(request,'home/signup.html')
    


def homepage(request):
    context={
        'posts':posts.objects.all()
    }
    return render(request,'home/homepage.html', context)

@login_required
def newpost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        newpost = models.posts(title=title, content=content,author=request.user)
        newpost.save()
        return redirect('/homepage')
    # else:
    #     if 'next' in request.GET:
    #         messages.warning(request, "You nseed to login to access that page.")
    return render(request,'home/newpost.html')

def mypost(request):
    context={
        'posts': posts.objects.filter(author = request.user)
    }
    return render(request,'home/mypost.html', context)


def signout(request):
    logout(request)
    return redirect('login')
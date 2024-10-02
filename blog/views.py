from django import forms
from django.contrib.auth import authenticate
from django.shortcuts import render,HttpResponseRedirect
from .forms import LoginForm, SignupForm,PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib .auth import authenticate,login,logout
from.models import Post
from django.contrib.auth.models import User
import logging
import sys, os

logger = logging.getLogger(__name__)
logger = logging.getLogger('django')
logger_demo = logging.getLogger('demo_log')
logger_post = logging.getLogger('post_log')


#Home
def Home(request):
    # Import Logging library 
    logger.info("I print on the console and also on info.log upper")
    logger.error("I print on the console and also on info.log upper")
    logger_demo.info("I print on demo.log upper")
    logger_demo.error("I print on demo.log upper")
    logger_post.info("I print on post.log upper")
    logger_post.error("I print on post.log upper")
    posts=Post.objects.all()
    return render(request,'blog/home.html',{"posts":posts})

#About
def About(request):
    logger_demo.info("I print about page on demo.log upper")
    logger_demo.error("I print about page on demo.log upper")
    return render(request,'blog/about.html')

#Contact
def Contact(request):
    try:
        raise Exception('Error')
    except Exception as e:
        # logger_post.error('Hiii')
        # exc_type, exc_obj, exc_tb= sys.exc_info()
        # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        logger_post.error(str(e))             #exc_type, fname, exc_tb.tb_lineno, 
        print(e)
    return render(request,'blog/contact.html')

#Dashboard
def Dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        return render(request,'blog/dashboard.html',{"posts":posts})
    else:
        return HttpResponseRedirect("/login/")

#logout
def User_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

#signup
def User_Signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            un=form.cleaned_data['username']
            print(un)
            messages.success(request,'Congratulation !! You have become author')
            form.save()
    else:
        form=SignupForm()
    return render(request,'blog/signup.html',{"form":form})

#login
def Login(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            form=LoginForm(request.POST,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username'] 
                upass=form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'logged in successfully !!')
                    return HttpResponseRedirect("/dashboard/")
        else:
            form=LoginForm()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect("/dashboard/")

    
#Add_New_Post
def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                pst=Post(title=title,desc=desc)
                pst.save()
                form=PostForm()
        else:
            form=PostForm()            
        return render(request,"blog/addpost.html",{'form':form})
    else:
        return HttpResponseRedirect("/login/")


#Update_Post
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi =Post.objects.get(pk=id)
            form= PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)
        return render(request,"blog/updatepost.html",{'form':form})
    else:
        return HttpResponseRedirect("/login/")

#Delete_Post
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect("/dashboard/")
    else:
        return HttpResponseRedirect("/login/")
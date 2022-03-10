from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm

# Create your views here.


#Home
def Home(request):
    return render(request,'blog/home.html')

#About
def About(request):
    return render(request,'blog/about.html')

#Contact
def Contact(request):
    return render(request,'blog/contact.html')

#Dashboard
def Dashboard(request):
    return render(request,'blog/dashboard.html')

#logout
def User_logout(request):
    return HttpResponseRedirect("/")

#signup
def User_Signup(request):
    form=SignupForm()
    return render(request,'blog/signup.html',{"form":form})

#login
def Login(request):
    return render(request,'blog/login.html')
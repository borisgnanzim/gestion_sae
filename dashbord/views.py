from django.shortcuts import render
from .models import *
#from django.template import 
from django.contrib.auth import login,authenticate,logout,decorators
from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
# def dashbord(request): 
#   return render(request, 'index.html'); 

def Login(request):
    if( request.method =='POST'):
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect("/dashbord")
        print("FAILED")
    return render(request,'login.html')

def Logout(request):
    logout(request)
    return redirect('/login')

@decorators.login_required(login_url='/login')
def dashbord(request): 
  return render(request, 'index.html'); 
 

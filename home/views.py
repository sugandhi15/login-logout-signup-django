from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.
#      User:sugandhi15     Password:suga$$$00
def index(request):
    try:
        if request.user.is_anonymous:
            redirect('/login')
        return render(request,'index.html')
    except Exception as e:
        return HttpResponse(e)

def login(request):
        # if user has enetered correct credentials
    try:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                return redirect('/')
            else:
                return render(request,'login.html')
        return render(request,'login.html')
    except Exception as e:
        return HttpResponse("Error occured")

def logout(request):
    try:
        logout(request)
        return redirect('/login')
    except Exception as e:
        return HttpResponse(e)
    
def signup(request):
    try:
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.create_user(username=username,password=password)
            user.save()
            return HttpResponse("saved")
        return render(request,'signup.html')
    except Exception as e:
        return HttpResponse("Error Occured",e)

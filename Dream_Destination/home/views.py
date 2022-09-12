
from http.client import HTTPResponse
from tkinter.messagebox import NO
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import product
from django.contrib.auth.models import auth,User
def index(request):
    return render(request,"index.html")
    
def login(request):
    if request.method =='POST':
        uname=request.POST['uname']
        pname=request.POST['pname']
        user=auth.authenticate(username=uname,password=pname)
        if user is not None:
            auth.login(request,user)    
            return redirect('/')
        else:
            return render(request,"login.html",{'msg':'invalide username and password'})
    else:        
        return render(request,"login.html")
def register(request):
    if request.method =='POST':
        uname=request.POST['username']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        ename=request.POST['email']
        passname=request.POST['passname']
        namep=request.POST['namep']
        ucheck=User.objects.filter(username=uname)
        echeck=User.objects.filter(email=ename)
        if ucheck:
            return render (request,"register.html",{'msg':'username is already taken'})
        elif echeck:
            return render(request,"register.html",{'msg':'email is already taken'})
        elif namep !=passname:     
            return render (request,'register.html',{'msg':'incorrect password'})
        else:     
            user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=ename,password=passname)
            user.save();
            return redirect('/')
    else:
        return render(request,"register.html")



   
    
def logout(request):
    auth.logout(request)
    return redirect('/')
    


p1=product()
p1.name="spring"
p1.price=100
p1.description="asdfghjklzxcvbnmqwertyuiop"
p2=product()
p2.name="sweets"
p2.price=150
p2.description="qwertyiopcvbnmcvbnmqwer"
p3=product()
p3.name="polish"
p3.price=120
p3.description="ghjklxcvbnmmertyuisdfgasqw"
p4=product()
p4.name="galaxy"
p4.price=300
p4.description="ljhgfdsapoiuytrewqzxcvbnm"

pro=[p1,p2,p3,p4]

def samp(request):
    return render(request,"test.html",{'a':pro}) 
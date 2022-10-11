
from ctypes.wintypes import MSG
from http.client import HTTPResponse
from socket import MSG_BCAST
from tkinter.messagebox import NO
from django.shortcuts import render,redirect
from django.http import HttpResponse
from product.models import TravellPlace
from django.contrib.auth.models import auth,User


def index(request):
    #cookies_view
    if 'pro_name' in request.COOKIES:
        msg=request.COOKIES['pro_name']
    else:
        msg=" What Say Our Clients"
    #searching
    if request.method=="POST":
        val=request.POST["search_box"]
        data=TravellPlace.objects.filter(name__istartswith=val)
    else:
        data=TravellPlace.objects.all()
    return render(request,"index.html",{'as':data,'msg':msg})

  
    
def login(request):
    if request.method =='POST':
        uname=request.POST['uname']
        pname=request.POST['pname']
        user=auth.authenticate(username=uname,password=pname)
        if user is not None:
            auth.login(request,user)    
            res=redirect('/')
            res.set_cookie('name',uname)
            return res
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


def samp(request):
    return render(request,"test.html",{'a':pro}) 
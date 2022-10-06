from cgi import test
from django.shortcuts import render,redirect
from .models import TravellPlace,comments
from django.http import JsonResponse
from django.core.cache import cache
# Create your views here.


def details(request):
    a=request.GET['id']
    if cache.get(id):
        pro=cache.get(id)
        print("data from cache")
    else:
        pro=TravellPlace.objects.get(id=a)
        cache.set(id,pro)
        print("data from database")
    cmt=comments.objects.filter(place_id=a) #for comments loading
    return render(request,"single.html",{'p':pro,'cmt':cmt})

def commt(request):
    user=request.GET['user']
    place=request.GET['pro_id']
    msg=request.GET['msg']
    cmt=comments.objects.create(cmt=msg,name=user,place_id=place) #for comments adding
    cmt.save();
    return redirect('/')    


def search(request):
    a=request.POST['homepage']
    obj=TravellPlace.objects.filter(name__istartswith=a)
    print(obj)
    return render(request,"index.html",{'s':a})    
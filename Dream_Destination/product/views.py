
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
    res=render(request,"single.html",{'p':pro,'cmt':cmt})
    res.set_cookie('pro_name',pro.name)
    return res


def details2(request):
    a=request.GET['id']
    
    if "recent" in request.session:
        
        if a in request.session['recent']:
               request.session['recent'].remove(a)
        request.session['recent'].insert(0,a)
        if len(request.session['recent'])>4:
            request.session['recent'].pop()
        place=TravellPlace.objects.filter(id__in=request.session['recent'])
        print(request.session['recent'])
        print(place)
    else:
        request.session['recent']=[a]
        place=TravellPlace.objects.filter(id=a)
    request.session.modified=True
    pro=TravellPlace.objects.get(id=a)    
    cmt=comments.objects.filter(place_id=a)  
    return render(request,"single.html",{'p':pro,'cmt':cmt,'place2':place})


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
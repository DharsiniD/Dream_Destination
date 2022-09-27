from django.shortcuts import render,redirect
from .models import TravellPlace,comments
# Create your views here.
def details(request):
    a=request.GET['id']
    pro=TravellPlace.objects.get(id=a)
    cmt=comments.objects.filter(place_id=a)
    return render(request,"single.html",{'p':pro,'cmt':cmt})

def commt(request):
    user=request.GET['user']
    place=request.GET['pro_id']
    msg=request.GET['msg']
    cmt=comments.objects.create(cmt=msg,name=user,place_id=place)
    cmt.save();
    return redirect('/')    
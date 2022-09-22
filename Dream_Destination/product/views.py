from django.shortcuts import render
from .models import TravellPlace
# Create your views here.
def details(request):
    a=request.GET['id']
    pro=TravellPlace.objects.get(id=a)
    return render(request,"single.html",{'p':pro})
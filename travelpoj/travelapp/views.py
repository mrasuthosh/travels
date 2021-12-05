from django.shortcuts import render
from . models import travelus , travelteem
# Create your views here.

def travel(request):
    obj =travelus.objects.all()
    objs = travelteem.objects.all()
    return render(request,'index.html',{'obj':obj,'objs':objs})
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import student
import requests,json


def index(request):
    if request.method=="POST":
        firstname=request.POST['fname']
        lastname=request.POST['lname']

        r=requests.get('http://api.icndb.com/jokes/random?firstName='+ firstname + '&lastName=' + lastname)
        data=json.loads(r.text)
        r=data.get('value').get('joke')
        context={'joke':r}
        return render(request,'home.html',context)
    else:
        firstname='mukesh'
        lastname='goud'

        r=requests.get('http://api.icndb.com/jokes/random?firstName='+ firstname + '&lastName=' + lastname)
        data=json.loads(r.text)
        r=data.get('value').get('joke')
        context={'joke':r}
        return render(request,'home.html',context)

def portfolio(request):
    return render(request,'portfolio.html')
def fb(request):
    return render(request,'fb.html')
def whatsapp(request):
    return render(request,'bunny.html')
def contact(request):
    return render(request,'bunny.html')
def insta(request):
    return render(request,'contact.html')
def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']

        std=student(first_name=first_name,last_name=last_name)
        std.save();

        return redirect('fb')
    else:
        return render(request,'fb.html')


# Create your views here.

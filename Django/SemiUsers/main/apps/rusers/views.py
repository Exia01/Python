from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import localtime, strftime
from django.utils.crypto import get_random_string
from django.conf.urls.static import static
from .models import *




def index(request):
    return render(request, 'index.html', {"info": User.objects.all()})


def show(request, x):
    return render(request, 'showuser.html', {"user":User.objects.get(id=x)})


def edit(request, x):
    return render(request, 'edit.html', {"user":User.objects.get(id=x)})


def update(request, x):
    errors = User.objects.validator(request.POST) 
    print(errors)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('edit/',)
    else:  
        b = User.objects.get(id=x)
        b.fname = request.POST['fname']
        b.lname = request.POST['lname']
        b.email = request.POST['email']
        b.save()
        messages.success(request, "User Successfully Updated")
    return redirect("/")


def add(request):
    return render(request, 'adduser.html')


def process(request):
    print(request.POST)
    results = User.objects.validator(request.POST)
    if results:
        for key, value in results.items():
            messages.message(request, value, extra_tags=key)
        return redirect("/add")
    else:
        User.objects.create(
            fname=request.POST['fname'], lname=request.POST['lname'], email=request.POST['email'])
        return redirect("/")

def delete(request, x):
    b = User.objects.get(id=x)
    b.delete()
    return redirect('/') 

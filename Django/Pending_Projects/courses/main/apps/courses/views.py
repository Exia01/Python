from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    # Product.objects.all().delete()
    # Sales.objects.all().delete()
    return render(request, 'courses/index.html', {'info': Course.objects.all()})


def addbooks(request):
    results = Course.objects.BookValidator(request.POST)
    print(results)

    if results[0]:
        return redirect('/')
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error)

        return redirect('/')

def remove(request, x):
    return render(request,'courses/remove', {"info":Course.objects.get(id=x)}) 

from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def indexlogin(request):
    # Product.objects.all().delete()
    # Sales.objects.all().delete()
    return render(request, 'xapp/login.html')


def register(request):
    return render(request, 'xapp/register.html')


def create(request):
    print(request.POST)
    results = User.objects.regValidator(request.POST)
    # print(results)
    if results[0]:
        request.session['id'] = results[1].id
        request.session['fname'] = results[1].fname
        return redirect('/')
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR,error, extra_tags='register')
            return redirect('/register')
            
def landing(request):
    return render(request, 'xapp/landing.html')


def loginprocess(request):
   
    results = User.objects.loginValidator(request.POST)
    # print(results)

    if results[0]:
        request.session['id'] = results[1].id
        request.session['fname'] = results[1].fname

        # return redirect('/dashboard')
        return redirect('/dashboard')
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error, extra_tags='login')
        return redirect('/')

from django.shortcuts import render, HttpResponse, redirect
from .models import Blog
from django.contrib import messages
from time import localtime, strftime
from django.utils.crypto import get_random_string
from django.conf.urls.static import static


def index(request): 
   
    if 'count' not in request.session:
        request.session['count'] = 0
      
    return render(request, 'start/index.html')


def process(request): 
    print('all good bruhh')
    if request.method == 'POST':
        request.session['Name'] = request.POST['Name']
        request.session['opt1'] = request.POST['opt1']
        request.session['opt2'] = request.POST['opt2']
        request.session['Comments'] = request.POST['Comments']
        return redirect('/result')
    else:
        return redirect('/')

def results(request):
      return render(request, 'start/results.html')

def clear(request):
    return redirect("/")



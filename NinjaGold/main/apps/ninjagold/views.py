from django.shortcuts import render, HttpResponse, redirect 
from django.conf.urls.static import static

def index(request):
    return render(request, 'index.html')

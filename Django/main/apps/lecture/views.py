from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import localtime, strftime
from django.utils.crypto import get_random_string
from django.conf.urls.static import static


def index(request):
    context = {
        "email": "Rickjames@gmail.com",
        "name": "Rick James"
    }
    return render(request, "lecture/index2.html", context)


def blog(request):
    return render(request, 'lecture/index.html ')


def create(request):
    if request.method == "POST" or "GET":
        # print("*"*50)
        # print(request.POST)
        # print(request.POST['name'])
        # print(request.POST['desc'])
        # request.session['name'] = "test"  # more on session below
        # print(request.session['name'])
        # print("*"*50)
        return redirect("/")
    else:
        return redirect("/")

def timenow(request):
    info = {
        "time": strftime("%Y-%m-%d %H:%M %p", localtime())
    }
    return render(request, 'lecture/index3.html', info)


def wordnow(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'Rword' not in request.session:
        request.session['Rword'] = ""
    
    return render(request, 'lecture/word.html', )


def generate(request):
    if request.method == "POST":
        request.session['count'] +=1 
        request.session['Rword']  = get_random_string(length=32) #wordup!
        return redirect("/word_generator")
    else:
        return redirect("/word_generator")

def destroy(request):
    request.session.clear
    return redirect("/word_generator")

# def index(request):
    # print(strftime('%Y-%m-%d %H:%M:%S', gmtime()))
    # print get_random_string(length=14)
    # return render(request, 'lecture/index.html ')


# The line below goes into the html

# {% load static %}
#    The line above tells Django to be ready to listen for static files
#      <link rel="stylesheet" href="{% static 'lecture/css/main.css' %}">
#       Put the static files in the static folder inside your app.
#            Django collects files within all static folders and puts them within a single folder

from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, 'first_app/index.html ')

    #response = "Ellow there, I am your first request!"
    #return HttpResponse(response)


def test(request): 
    response = "Eyyyy! I am test :o"
    return HttpResponse(response)

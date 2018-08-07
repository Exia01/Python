from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import localtime, strftime
from django.conf.urls.static import static
info = {
    'inventory': [
        {'id': 1, 'name': 'Dojo T-shirt', 'price': 19.99},
        {'id': 2, 'name': 'Dojo Sweater', 'price': 29.99},
        {'id': 3, 'name': 'Dojo Cup', 'price': 4.99},
        {'id': 4, 'name': 'Algorithm Book', 'price': 49.99},
    ],
    'checkrange': [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ]
}


def index(request):
    return render(request, 'index.html', info)


def process(request):
    if request.method == "POST":
        if 'count' not in request.session:
            request.session['count'] = 0
        if 'total' not in request.session:
            request.session['total'] = 0
        if 'sub' not in request.session:
            request.session['sub'] = 0
        for i in info['inventory']:
            request.session['count'] += int(request.POST[str(i['id'])])
            request.session['sub'] += int(request.POST[str(i['id'])]) * i['price']
        if request.session['count'] == 0 or request.session['sub'] == 0:
            return redirect('/')
        request.session['total'] += request.session['sub']
        return redirect('/result')
    else:
        return redirect('/')


def results(request):
    return render(request, 'results.html')


def clear(request):
    request.session['count'] = 0
    request.session['total'] = 0
    request.session['sub'] = 0
    return redirect("/")

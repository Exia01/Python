from django.shortcuts import render, redirect


def home_page(req):
    context = {
        'title': 'Hello World!',
        'content': 'Welcome to the home page!'
    }
    return render(req, "home_page.html", context)


def about_page(req):
    context = {
        'title': 'About Page!',
        'content': 'Welcome to the about page!'
    }
    return render(req, "home_page.html", context)


def contact_page(req):
    context = {
        'title': 'Contact Page!',
        'content': 'Welcome to the contact page!'
    }
    if req.method == 'POST':
        # print(req.POST)
        print(req.POST.get('full_name'))
        print(req.POST.get('email'))
        print(req.POST.get('content'))
    return render(req, "contact/contact_page.html", context)


def dashboard_page(req):
    context = {
        'title': 'Dashboard Page!',
        'content': 'Welcome to the dashboard page!'
    }
    return render(req, "home_page.html", context)

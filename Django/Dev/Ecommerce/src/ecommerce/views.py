from django.contrib.auth import (authenticate, login, get_user_model)
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(req):
    # print(req.session.get("first_name", "Guest"))
    context = {
        'title': 'Hello World!',
        'content': 'Welcome to the home page!',
    }
    if req.user.is_authenticated:
        context['premium_content'] = 'YEaaaa buddy!'
    return render(req, "home_page.html", context)


def about_page(req):
    context = {
        'title': 'About Page!',
        'content': 'Welcome to the about page!'
    }
    return render(req, "home_page.html", context)


def contact_page(req):
    contact_form = ContactForm(req.POST or None)  # Creating an instance
    context = {
        'title': 'Contact Page!',
        'content': 'Welcome to the contact page!',
        'form': contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if req.method == 'POST':
    #     # print(req.POST)
    #     print(req.POST.get('full_name'))
    #     print(req.POST.get('email'))
    #     print(req.POST.get('content'))
    return render(req, "contact/contact_page.html", context)


def login_page(req):
    form = LoginForm(req.POST or None)  # instanciating a form
    context = {
        'form': form,
        'content': 'Welcome to the login page!',
    }
    print("User Logged in", req.user.is_authenticated)
    if form.is_valid():
        # print(form.cleaned_data)
        # using global user object
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(req, username=username,
                            password=password)  # extracts the user
        if user is not None:
            login(req, user)  # this logs in the user
            # Redirect to a success page.
            context['form'] = LoginForm()  # resets the session
            print("User Logged in", req.user.is_authenticated)
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            print('Error')
    return render(req, "auth/login.html", context)


User = get_user_model()


def register_page(req):
    form = RegisterForm(req.POST or None)  # instanciating a form
    # print(form)
    # print(req.post)
    context = {
        'form': form,
        'content': 'Welcome to the register page!'
    }
    if form.is_valid():
        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        newUser = User.objects.create_user(username, email, password)
        print(newUser)
    return render(req, "auth/login.html", context)


def dashboard_page(req):
    context = {
        'title': 'Dashboard Page!',
        'content': 'Welcome to the dashboard page!'
    }
    return render(req, "home_page.html", context)

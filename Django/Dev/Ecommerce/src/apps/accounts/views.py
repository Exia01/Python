from django.contrib.auth import (authenticate, login, get_user_model)
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, GuestForm
from django.utils.http import is_safe_url
from .models import GuestEmail

def guest_register_view(req):
    form = GuestForm(req.POST or None)  # instanciating a form
    context = {
        'form': form,
        'content': 'Welcome to the login page!',
    }
    next_ = req.GET.get('next')
    next_post = req.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email = form.cleaned_data.get('email')
        new_guest_email = GuestEmail.objects.create(email=email)
        req.session['guest_email_id'] = new_guest_email.id
        # print('from guest', new_guest_email)
        if is_safe_url(redirect_path, req.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('account:register')
    return redirect("account:register")

def login_page(req):
    form = LoginForm(req.POST or None)  # instanciating a form
    context = {
        'form': form,
        'content': 'Welcome to the login page!',
    }
    next_ = req.GET.get('next')
    next_post = req.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(req, username=username,
                            password=password)  # extracts the user
        if user is not None:
            login(req, user)  # this logs in the user
            try:
                del req.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, req.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/')
        else:
            print('Error')
    return render(req, "accounts/login.html", context)


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
    return render(req, "accounts/login.html", context)

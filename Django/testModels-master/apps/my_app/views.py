from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(req):
    return render(req, 'my_app/index.html')


def process(req):
    # print(req.POST)

    results = Owner.objects.validator(req.POST)
    # print(results)

    if results[0]:
        # save id in session (which is in results[1])
        # (True, owner_object)

        req.session['id'] = results[1].id
        req.session['name'] = results[1].fname

        return redirect('/success')
    else:
        # transfer errors to flash messages (also in results[1])
        # (False, errors)

        for error in results[1]:
            messages.add_message(req, messages.ERROR, error)

        return redirect('/')


def success(req):
    return render(req, 'my_app/success.html')

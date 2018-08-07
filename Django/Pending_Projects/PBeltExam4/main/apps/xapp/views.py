from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from datetime import date

today = date.today()

def indexlogin(request):
    return render(request, 'xapp/login.html')


def register(request):
    return render(request, 'xapp/register.html')


def createuser(request):
    results = User.objects.regValidator(request.POST)
    print(results)
    if results[0]:
        request.session['id'] = results[1].id
        request.session['name'] = results[1].name
        return redirect('/dashboard')
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error, extra_tags='register')
            return redirect('/register')


def loginprocess(request):
    results = User.objects.loginValidator(request.POST)
    if results[0]:
        request.session['id'] = results[1].id
        request.session['name'] = results[1].name
        return redirect('/dashboard')
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error, extra_tags='login')
        return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/')


def dashboard(request, user_id=None):
    if 'id' not in request.session:
        return redirect('/')

    currenttasks = Appointment.objects.filter(date=today).order_by('hour')

    context = {
        'currenttasks' : currenttasks,
    }

    return render(request, 'xapp/dashboard.html', context)




def add(request, user_id=None):
    results = Appointment.objects.appointmentValidator(request.POST, request.session['id'])
    print(results)
    if results[0]:
        return redirect('/dashboard/{}'.format(request.session['id']))
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error, extra_tags='adderror')
            return redirect('/dashboard/{}'.format(request.session['id']))


def delete(request, x):
    Appointment.objects.get(id=x).delete()
    return redirect('/dashboard')


def update(request, x):
    results = Appointment.objects.appointmentValidator(request.POST, request.session['id'])

    if results[0]: 
        b = Appointment.objects.get(id=x)
        b.task = request.POST['task']
        b.status = request.POST['status']
        b.hour = request.POST['hour']
        b.date = request.POST['date']
        b.date = request.POST['time']
        b.save()
        messages.success(request, "User Successfully Updated")
        return redirect('/dashboard')
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error, extra_tags='adderror')
            return redirect('/dashboard/{}'.format(request.session['id']))


def edit(request, x):
    return render(request, 'xapp/edit.html', {"appoinment":Appointment.objects.get(id=x)})

# def remove(request, x):
#     user = User.objects.get(id=request.session['id']) 
#     appointment = Appointment.objects.get(id=x)
#     user.wishitems.remove(appointment)
    
#     return redirect('/dashboard')


# def showproduct(request, x):
#     product = Product.objects.get(id=x)
#     other_users = product.wisher.all()
#     context = {
#         'product' : product,
#         'other_users' : other_users
#     }
#     return render(request, 'xapp/showproduct.html', context)


# def addtowish(request, x):
#     user = User.objects.get(id=request.session['id'])
#     product = Product.objects.get(id=x)

#     user.wishitems.add(product)
    
#     return redirect('/dashboard')

#Appointment.objects.filter(client = request.session['id']).order_by('hour')

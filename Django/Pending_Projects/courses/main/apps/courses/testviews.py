from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


# Create your views here.
def index(request):
    
    return render(request,'login/index.html')

def register(request):
    results = User.objects.regValidator(request.POST)
    print(results)
    
    if results[0]:
        request.session['id'] = results[1].id
        request.session['name'] = results[1].fname
        return redirect('/dashboard')
    else:
        for error in results[1]:
            messages.add_message(request,messages.ERROR, error, extra_tags='register')
        return redirect('/')

def login(request):
    results = User.objects.loginValidator(request.POST)
    print(results)
    if results[0]:
        request.session['id'] = results[1].id
        request.session['name'] = results[1].fname
        return redirect('/dashboard/{}'.format(request.session['id']))
    else:
        for error in results[1]:
           messages.add_message(request, messages.ERROR, error, extra_tags='login')
        return redirect('/')

def dashboard(request,id=None):
    if 'id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session["id"])
    context = {
        "items" : Items.objects.select_related("creator").filter(creator=request.session['id']),
        # "me" : Items.objects.filter(creator=user).Item.objects.filter(adder__id=user.id).distinct(),
        "notme" : Items.objects.filter,
        # "notme": Item.objects.all().exclude(creator=user).exclude(adders__id=user.id)
    }   
    return render(request,'login/dashboard.html',context)

def add(request):
    if 'id' not in request.session:
        return redirect('/')
    return render(request,'login/add.html')

def create(request):
    if 'id' not in request.session:
        return redirect('/')

    if len(request.POST["item_name"]) > 3:
        user = User.objects.get(id=request.session['id'])
        item = request.POST["item_name"]
        Items.objects.create(name=item, creator=user)
        return redirect('/add')

    else:
        messages.add_message(request, messages.ERROR, "Your Item Needs to Be Longer Than 3 Characters ")
        return redirect('/add')

def show(request,id):
    if 'id' not in request.session:
        return redirect('/')
    context = {
        "items" : Items.objects.get(id=id),
        "users" : User.objects.all()
    }
    return render(request,'login/show.html',context)

def delete(request,id):
    item = Items.objects.get(id=id)
    item.delete()
    return redirect('/dashboard/{}'.format(request.session['id']))

def logout(request):
    del request.session['id']
    return redirect('/')
    



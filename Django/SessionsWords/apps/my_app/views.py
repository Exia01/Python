from django.shortcuts import render, redirect


def index(req):
    if 'visits' not in req.session:
        req.session['visits'] = 1
    else:
        req.session['visits'] += 1
    return render(req, 'my_app/index.html')


def process(req):
    print(req.POST)

    if 'words' not in req.session:
        req.session['words'] = [req.POST]
    else:
        temp_list = req.session['words']
        temp_list.insert(0, req.POST)
        req.session['words'] = temp_list

    return redirect('/')


def clear(req):
    req.session.clear()
    return redirect('/')

from django.shortcuts import render, HttpResponse, redirect


def index(request):
    response = 'Placeholder to later display all the list of blogs.'
    # we can create a response variable and pass it
    return HttpResponse(response)


def new(request):
    response = 'Placeholder to display a new form to create a new blog'
    return HttpResponse(response)


def create(request):
    return redirect('/blogs')


# or alternatively we can pass it on directly onto the response


def number(request, number):
    return HttpResponse('Placeholder to display blog ' + number)


def number_edit(request, number):
    return HttpResponse('Placeholder to edit blog ' + number)


def number_delete(request, number):
    return HttpResponse('Placeholder to delete blog ' + number)

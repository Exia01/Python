from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import localtime, strftime
from django.utils.crypto import get_random_string
from django.conf.urls.static import static
from .models import Blog

from django.shortcuts import render, HttpResponse, redirect
from .models import Blog

# pass the post data to the method we wrote and save the response in a variable called errors
# # check if the errors object has anything in it  
# # if the errors object contains anything, loop through each key-value pair and make a flash message 
# # redirect the user back to the form to fix the errors
# # if the errors object is empty, that means there were no errors!        
# retrieve the blog to be updated, make the changes, and save


def update(request, id):
    errors = Blog.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/blog/edit/'+id)
    else:
        blog = Blog.objects.get(id=id)
        blog.name = request.POST['name']
        blog.desc = request.POST['desc']
        blog.save()
        messages.success(request, 'Blog successfully updated')
        return redirect('/blogs')
    # redirect to a success route

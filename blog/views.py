from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.conf import settings
import datetime
import os
from django.contrib.auth.models import User
from _mysql import result
from html5lib.treewalkers._base import to_text
from django.contrib.auth import authenticate

# Create your views here.
def addArticaleForm(request):
    #adding article is depending on user's rolles --> Sarah
    user = request.user
    if user.is_staff or user.is_superuser:
        #Salma
        return render(request, 'blog/addArtical.html')
    else :
        return render(request, 'blog/permissionDenied.html')

def updateArticaleForm(request, articale_id):
    #adding article is depending on user's rolles --> Sarah
    user = request.user
    if user.is_staff or user.is_superuser:
        return render(request, 'blog/updateArticale.html', {'articale_id':articale_id})
    else :
        return render(request, 'blog/permissionDenied.html')

def deleteArticaleForm(request, articale_id):
    #adding article is depending on user's rolles --> Sarah
    user = request.user
    if user.is_staff or user.is_superuser:
        #salma
        return render(request, 'blog/deleteArticale.html', {'articale_id':articale_id})
    else :
        return render(request, 'blog/permissionDenied.html')

def addArticale(request):
    content = request.POST['content']
    title = request.POST['title']
    if request.FILES.has_key('img') :
        image = request.FILES['img']
    else:
        image = ''
    c = Articles(article_content=content, article_title=title, article_creationDate=datetime.datetime.now(), article_image=image)
    c.save()    
    #adding article is depending on user's rolles --> Sarah
    user = request.user
    if user.is_staff or user.is_superuser:
        #Salma
        return render(request, 'blog/addArtical.html')
    else :
        return render(request, 'blog/permissionDenied.html')

#Salma
def updateArticale(request, articale_id):
    articale = Articles.objects.get(pk=articale_id)
    if articale.article_image :
        os.remove(os.path.join(settings.MEDIA_ROOT, articale.article_image.name))
    articale.article_title = request.POST['title']
    articale.article_content = request.POST['content']
    articale.article_image = request.FILES['img']
    articale.save()    
    #adding article is depending on user's rolles --> Sarah
    user = request.user
    if user.is_staff or user.is_superuser:
        #salma
        return render(request, 'blog/addArtical.html')
    else :
        return render(request, 'blog/permissionDenied.html')

def deleteArticale(request, articale_id):
    articale = Articles.objects.get(pk=articale_id)
    if articale.article_image :
        os.remove(os.path.join(settings.MEDIA_ROOT, articale.article_image.name))
    articale.delete()    
    #adding article is depending on user's rolles --> Sarah
    user = request.user
    if user.is_staff or user.is_superuser:
        #Salma
        return render(request, 'blog/addArtical.html')
    else :
        return render(request, 'blog/permissionDenied.html')

def selectAllArticales(request):
    articales = Articles.objects.all()
    result = '<ul>'
    for articale in articales :
        result += '<li>' + articale.article_title + '</li>'
    result += '</ul>'
    return HttpResponse(result)


# list all users --> Sarah
def listAllUsers(request):
    users = User.objects.all()
    result = "<table border='1'><th>First name</th>"
    result += "<th>Last name</th><th>username</th>"
    result += "<th>email</th><th>Last Login</th>"
    result += "<th>date joined</th><th>is active?</th>"
    result += "<th>is staff?</th><th>is super user?</th>"
    for user in users :
        result += '<tr><td>' + user.first_name + '</td>'
        result += '<td>' + user.last_name + '</td>'
        result += '<td>' + user.username + '</td>'
        result += '<td>' + user.email + '</td>'
        result += '<td>' + to_text(user.last_login) + '</td>'
        result += '<td>' + to_text(user.date_joined) + '</td>'
        result += '<td>' + to_text(user.is_active) + '</td>'
        result += '<td>' + to_text(user.is_staff) + '</td>'
        result += '<td>' + to_text(user.is_superuser) + '</td></tr>'
        
        
    result += "<table>"
    return HttpResponse(result)


# Login Part  With Sessions  -->  Shrouk (functions : home,signin)
def home(request):
    users = User.objects.all()
    try:
        for user in users:
            # check for username and pass in DB . 
            if (user.username == request.POST['u_name'] and user.password == request.POST['pass']):
            # the password verified for the user
                if user.is_active:
                    # User is valid, active and authenticated 
                    request.session["user_id"] = user.id
                    return render(request, 'blog/home.html',{'User':user})  
                else:
                    #The password is valid, but the account has been disabled!
                    return render(request, 'blog/activeAccount.html')               
    except:
        return render(request, 'blog/signin.html')              
    return render(request, 'blog/signin.html')

def signin(request):
    #check if the user logged in redirect to home page
    if "user_id" in request.session :
        return  render(request, 'blog/home.html')
    else:
        return render(request,'blog/signin.html')
    
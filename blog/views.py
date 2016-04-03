from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.conf import settings
import datetime
import os
from django.contrib.auth.models import User
from _mysql import result
from html5lib.treewalkers._base import to_text

# Create your views here.
def addArticaleForm(request):
	#adding article is depending on user's rolles --> Sarah
	#note: this role is for all articles, not for user's articles --> Sarah
	# user = User.objects.all()
	# if user.is_staff or user.is_superuser:
		#Salma
		return render(request, 'blog/addArtical.html')
	# else :
	# 	return render(request, 'blog/permissionDenied.html')

def updateArticaleForm(request, articale_id):
	#adding article is depending on user's rolles --> Sarah
	#note: this role is for all articles, not for user's articles --> Sarah
	# user = User.objects.all()
	# if user.is_staff or user.is_superuser:
		return render(request, 'blog/updateArticale.html', {'articale_id':articale_id})
	# else :
	# 	return render(request, 'blog/permissionDenied.html')

def deleteArticaleForm(request, articale_id):
	#adding article is depending on user's rolles --> Sarah
	#note: this role is for all articles, not for user's articles --> Sarah
	# user = User.objects.all()
	# if user.is_staff or user.is_superuser:
		#salma
		return render(request, 'blog/deleteArticale.html', {'articale_id':articale_id})
	# else :
	# 	return render(request, 'blog/permissionDenied.html')

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
	#note: this role is for all articles, not for user's articles --> Sarah
	# user = User.objects.all()
	# if user.is_staff or user.is_superuser:
		#Salma
	return render(request, 'blog/addArtical.html')
	# else :
	# 	return render(request, 'blog/permissionDenied.html')

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
	#note: this role is for all articles, not for user's articles --> Sarah
	# user = User.objects.all()
	# if user.is_staff or user.is_superuser:
		#salma
	return render(request, 'blog/addArtical.html')
	# else :
	# 	return render(request, 'blog/permissionDenied.html')

def deleteArticale(request, articale_id):
	articale = Articles.objects.get(pk=articale_id)
	if articale.article_image :
		os.remove(os.path.join(settings.MEDIA_ROOT, articale.article_image.name))
	articale.delete()	
	#adding article is depending on user's rolles --> Sarah
	#note: this role is for all articles, not for user's articles --> Sarah
	# user = User.objects.all()
	# if user.is_staff or user.is_superuser:
		#Salma
	return render(request, 'blog/addArtical.html')
	# else :
	# 	return render(request, 'blog/permissionDenied.html')

def selectAllArticales(request):
	articales = Articles.objects.all()
	result = '<ul>'
	for articale in articales :
		result += '<li>' + articale.article_title + '</li>'
	result += '</ul>'
	return HttpResponse(result)

def selectAnArticale(request,articale_id) :
	articale = Articles.objects.get(pk=articale_id)
	comments=articale.comments_set.all()
	return render(request, 'blog/singleArticale.html',{'articale':articale,'comments':comments})

def addComment(request,articale_id):
	comment = request.POST['comment']
	articale=Articles.objects.get(pk=articale_id)
	c = Comments(comment_content=comment, comment_creationDate=datetime.datetime.now(), article_id=articale)
	c.save()	
	return render(request, 'blog/addArtical.html')

def addReply(request,articale_id,comment_id):
	reply = request.POST['reply']
	articale=Articles.objects.get(pk=articale_id)
	comment=Comments.objects.get(pk=comment_id)
	c = Comments(comment_content=reply, comment_creationDate=datetime.datetime.now(), article_id=articale,parent_id=comment)
	c.save()	
	return render(request, 'blog/addArtical.html')

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




from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.conf import settings
import datetime
import os
from django.contrib.auth.models import User

# Create your views here.
def addArticaleForm(request):
	return render(request,'blog/addArtical.html')

def updateArticaleForm(request,articale_id):
	return render(request,'blog/updateArticale.html',{'articale_id':articale_id})

def deleteArticaleForm(request,articale_id):
	return render(request,'blog/deleteArticale.html',{'articale_id':articale_id})

def addArticale(request):
	content=request.POST['content']
	title=request.POST['title']
	if request.FILES.has_key('img') :
		image=request.FILES['img']
	else:
		image=''
	c=Articles(article_content=content,article_title=title,article_creationDate=datetime.datetime.now(), article_image=image)
	c.save()	
	return render(request,'blog/addArtical.html')

def updateArticale(request,articale_id):
	articale=Articles.objects.get(pk=articale_id)
	if articale.article_image :
		os.remove(os.path.join(settings.MEDIA_ROOT, articale.article_image.name))
	articale.article_title=request.POST['title']
	articale.article_content=request.POST['content']
	articale.article_image=request.FILES['img']
	articale.save()	
	return render(request,'blog/addArtical.html')

def deleteArticale(request,articale_id):
	articale=Articles.objects.get(pk=articale_id)
	if articale.article_image :
		os.remove(os.path.join(settings.MEDIA_ROOT, articale.article_image.name))
	articale.delete()	
	return render(request,'blog/addArtical.html')

def selectAllArticales(request):
	articales=Articles.objects.all()
	result='<ul>'
	for articale in articales :
		result+='<li>'+articale.article_title+'</li>'
	result+='</ul>'
	return HttpResponse(result)
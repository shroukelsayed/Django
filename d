[1mdiff --git a/blog/__init__.pyc b/blog/__init__.pyc[m
[1mindex a77cb4d..a9d217c 100644[m
Binary files a/blog/__init__.pyc and b/blog/__init__.pyc differ
[1mdiff --git a/blog/admin.pyc b/blog/admin.pyc[m
[1mindex 55ea280..93abdd7 100644[m
Binary files a/blog/admin.pyc and b/blog/admin.pyc differ
[1mdiff --git a/blog/apps.pyc b/blog/apps.pyc[m
[1mindex 70f72de..1ccd848 100644[m
Binary files a/blog/apps.pyc and b/blog/apps.pyc differ
[1mdiff --git a/blog/migrations/0001_initial.pyc b/blog/migrations/0001_initial.pyc[m
[1mindex b08c31c..544503d 100644[m
Binary files a/blog/migrations/0001_initial.pyc and b/blog/migrations/0001_initial.pyc differ
[1mdiff --git a/blog/migrations/__init__.pyc b/blog/migrations/__init__.pyc[m
[1mindex 7623df2..a5ab740 100644[m
Binary files a/blog/migrations/__init__.pyc and b/blog/migrations/__init__.pyc differ
[1mdiff --git a/blog/models.py b/blog/models.py[m
[1mindex 3adbb92..0b56b3b 100644[m
[1m--- a/blog/models.py[m
[1m+++ b/blog/models.py[m
[36m@@ -8,8 +8,8 @@[m [mclass Articles (models.Model):[m
     article_title=models.CharField(max_length=100)[m
     article_content=models.CharField(max_length=300)[m
     article_creationDate=models.DateTimeField()[m
[31m-    article_image=models.CharField(max_length=100)[m
[31m-    article_num_views=models.IntegerField()[m
[32m+[m[32m    article_image=models.ImageField(null=True,blank=True,upload_to="articales")[m
[32m+[m[32m    article_num_views=models.IntegerField(default=0)[m
     article_isPublished=models.BooleanField(default=False)[m
     article_isApproved=models.BooleanField(default=False)[m
 #    user_id=models.ForeignKey(User,on_delete=models.CASCADE)[m
[1mdiff --git a/blog/models.pyc b/blog/models.pyc[m
[1mindex 59652e5..b53f9df 100644[m
Binary files a/blog/models.pyc and b/blog/models.pyc differ
[1mdiff --git a/blog/views.py b/blog/views.py[m
[1mindex 91ea44a..026f307 100644[m
[1m--- a/blog/views.py[m
[1m+++ b/blog/views.py[m
[36m@@ -1,3 +1,52 @@[m
 from django.shortcuts import render[m
[32m+[m[32mfrom django.http import HttpResponse[m
[32m+[m[32mfrom .models import *[m
[32m+[m[32mfrom django.conf import settings[m
[32m+[m[32mimport datetime[m
[32m+[m[32mimport os[m
 [m
 # Create your views here.[m
[32m+[m[32mdef addArticaleForm(request):[m
[32m+[m	[32mreturn render(request,'blog/addArtical.html')[m
[32m+[m
[32m+[m[32mdef updateArticaleForm(request,articale_id):[m
[32m+[m	[32mreturn render(request,'blog/updateArticale.html',{'articale_id':articale_id})[m
[32m+[m
[32m+[m[32mdef deleteArticaleForm(request,articale_id):[m
[32m+[m	[32mreturn render(request,'blog/deleteArticale.html',{'articale_id':articale_id})[m
[32m+[m
[32m+[m[32mdef addArticale(request):[m
[32m+[m	[32mcontent=request.POST['content'][m
[32m+[m	[32mtitle=request.POST['title'][m
[32m+[m	[32mif request.FILES.has_key('img') :[m
[32m+[m		[32mimage=request.FILES['img'][m
[32m+[m	[32melse:[m
[32m+[m		[32mimage=''[m
[32m+[m	[32mc=Articles(article_content=content,article_title=title,article_creationDate=datetime.datetime.now(), article_image=image)[m
[32m+[m	[32mc.save()[m[41m	[m
[32m+[m	[32mreturn render(request,'blog/addArtical.html')[m
[32m+[m
[32m+[m[32mdef updateArticale(request,articale_id):[m
[32m+[m	[32marticale=Articles.objects.get(pk=articale_id)[m
[32m+[m	[32mif articale.article_image :[m
[32m+[m		[32mos.remove(os.path.join(settings.MEDIA_ROOT, articale.article_image.name))[m
[32m+[m	[32marticale.article_title=request.POST['title'][m
[32m+[m	[32marticale.article_content=request.POST['content'][m
[32m+[m	[32marticale.article_image=request.FILES['img'][m
[32m+[m	[32marticale.save()[m[41m	[m
[32m+[m	[32mreturn render(request,'blog/addArtical.html')[m
[32m+[m
[32m+[m[32mdef deleteArticale(request,articale_id):[m
[32m+[m	[32marticale=Articles.objects.get(pk=articale_id)[m
[32m+[m	[32mif articale.article_image :[m
[32m+[m		[32mos.remove(os.path.join(settings.MEDIA_ROOT, articale.article_image.name))[m
[32m+[m	[32marticale.delete()[m[41m	[m
[32m+[m	[32mreturn render(request,'blog/addArtical.html')[m
[32m+[m
[32m+[m[32mdef selectAllArticales(request):[m
[32m+[m	[32marticales=Articles.objects.all()[m
[32m+[m	[32mresult='<ul>'[m
[32m+[m	[32mfor articale in articales :[m
[32m+[m		[32mresult+='<li>'+articale.article_title+'</li>'[m
[32m+[m	[32mresult+='</ul>'[m
[32m+[m	[32mreturn HttpResponse(result)[m
\ No newline at end of file[m
[1mdiff --git a/django_project/__init__.pyc b/django_project/__init__.pyc[m
[1mindex 11750c3..08604fb 100644[m
Binary files a/django_project/__init__.pyc and b/django_project/__init__.pyc differ
[1mdiff --git a/django_project/settings.py b/django_project/settings.py[m
[1mindex 0efd5ee..a4ae6be 100644[m
[1m--- a/django_project/settings.py[m
[1m+++ b/django_project/settings.py[m
[36m@@ -56,7 +56,7 @@[m [mROOT_URLCONF = 'django_project.urls'[m
 TEMPLATES = [[m
     {[m
         'BACKEND': 'django.template.backends.django.DjangoTemplates',[m
[31m-        'DIRS': [],[m
[32m+[m[32m        'DIRS': ['templates'],[m
         'APP_DIRS': True,[m
         'OPTIONS': {[m
             'context_processors': [[m
[36m@@ -71,7 +71,8 @@[m [mTEMPLATES = [[m
 [m
 WSGI_APPLICATION = 'django_project.wsgi.application'[m
 [m
[31m-[m
[32m+[m[32mMEDIA_ROOT = os.path.join(BASE_DIR, 'images/')[m
[32m+[m[32mMEDIA_URL  = '/images/'[m
 # Database[m
 # https://docs.djangoproject.com/en/1.9/ref/settings/#databases[m
 [m
[1mdiff --git a/django_project/settings.pyc b/django_project/settings.pyc[m
[1mindex 71f5b6b..7d0e1a2 100644[m
Binary files a/django_project/settings.pyc and b/django_project/settings.pyc differ
[1mdiff --git a/django_project/urls.py b/django_project/urls.py[m
[1mindex 916ffcf..2ef78eb 100644[m
[1m--- a/django_project/urls.py[m
[1m+++ b/django_project/urls.py[m
[36m@@ -15,7 +15,19 @@[m [mIncluding another URLconf[m
 """[m
 from django.conf.urls import url[m
 from django.contrib import admin[m
[32m+[m[32mfrom blog.views import *[m
 [m
 urlpatterns = [[m
     url(r'^admin/', admin.site.urls),[m
[32m+[m[32m    url(r'^addArticale/$', addArticale),[m
[32m+[m[32m    url(r'^addArticaleForm/$', addArticaleForm),[m
[32m+[m
[32m+[m[32m    url(r'^updateArticale/(?P<articale_id>[0-9]+)$', updateArticale),[m
[32m+[m[32m    url(r'^updateArticaleForm/(?P<articale_id>[0-9]+)$', updateArticaleForm),[m
[32m+[m
[32m+[m[32m    url(r'^deleteArticale/(?P<articale_id>[0-9]+)$', deleteArticale),[m
[32m+[m[32m    url(r'^deleteArticaleForm/(?P<articale_id>[0-9]+)$', deleteArticaleForm),[m
[32m+[m
[32m+[m[32m    url(r'^selectAllArticales/$', selectAllArticales),[m
[32m+[m[32m    url(r'^getAnArticale/(?P<articale_id>[0-9]+)$', getAnArticale),[m
 ][m
[1mdiff --git a/django_project/urls.pyc b/django_project/urls.pyc[m
[1mindex 8f03106..d175f15 100644[m
Binary files a/django_project/urls.pyc and b/django_project/urls.pyc differ
[1mdiff --git a/django_project/wsgi.pyc b/django_project/wsgi.pyc[m
[1mindex 40cf5ca..30208b6 100644[m
Binary files a/django_project/wsgi.pyc and b/django_project/wsgi.pyc differ

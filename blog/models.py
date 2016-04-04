from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articles (models.Model):
    
    article_title=models.CharField(max_length=100)
    article_content=models.CharField(max_length=300)
    article_creationDate=models.DateTimeField()
    article_image=models.ImageField(null=True,blank=True,upload_to="articales")
    article_num_views=models.IntegerField(default=0)
    article_isPublished=models.BooleanField(default=False)
    article_isApproved=models.BooleanField(default=False)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    def __unicode__(self):
        return self.article_title

class Comments (models.Model):
    
    comment_content=models.CharField(max_length=100)
    comment_creationDate=models.DateTimeField()
    comment_isApproved=models.BooleanField(default=False)
    article_id=models.ForeignKey(Articles,on_delete=models.CASCADE,default=1)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    parent_id=models.ForeignKey('self',default=id)

    def __unicode__(self):
        return self.article_title

class Tags (models.Model):
    tag_name=models.CharField(max_length=100)
    articleTag=models.ManyToManyField(Articles)

class Banwords (models.Model):
    word=models.CharField(max_length=100)


class Emotions (models.Model):
    keyword=models.CharField(max_length=100)
    path=models.CharField(max_length=100)
    

class System (models.Model):
    system_isLocked=models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    image = models.ImageField(upload_to='profile_images', blank=True)
    website = models.URLField(blank=True)
        
    
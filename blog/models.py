from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Articles (models.Model):
    
    article_title=models.CharField(max_length=100)
    article_content=models.CharField(max_length=300)
    article_creationDate=models.DateTimeField()
    article_image=models.CharField(max_length=100)
    article_num_views=models.IntegerField()
    article_isPublished=models.BooleanField(default=False)
    article_isApproved=models.BooleanField(default=False)
#    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

class Comments (models.Model):
    comment_content=models.CharField(max_length=100)
    comment_creationDate=models.DateTimeField()
    comment_isApproved=models.BooleanField(default=False)
    article_id=models.ForeignKey(Articles,on_delete=models.CASCADE,default=1)
#    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    parent_id=models.ForeignKey('self',default=id)

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
    
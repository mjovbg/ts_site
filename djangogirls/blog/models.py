from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
'''
Post
--------
title
text
author
created_date
published_date
====================
post should be able to be published. So it needs publish method.
'''

class Post (models.Model):          # models.Model tells django that this is a django model and it should be saved in DB
    # properties of the model (object)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   #foreign key is a link to another model
    title = models.CharField(max_length=200)
    text = models.TextField()           # text field is without limit
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        # with __str__() is called you get a string with a Post title

'''
A QuerySet is, in essence, a list of objects of a given Model. 
QuerySets allow you to read the data from the database, filter it and order it.
'''

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    # related_name allows to acces to comments from within the Post model.
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text



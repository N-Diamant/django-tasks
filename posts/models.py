from django.db import models

# Create your models here.

"""
class Post:
id int
title str(50)
content text
created datetime

"""

class Post(models.Model):
    title = models.CharField(max_length=50)
    contetnte = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def _str_(self) ->str: #this function is used to return string representation of the object
        return self.title

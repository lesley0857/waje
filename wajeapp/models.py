from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.TextField(null=True,max_length=200)
    last_name = models.TextField(null=True,max_length=200)

class Book(models.Model):
    name =  models.TextField(null=True,max_length=200)
    isbn = models.TextField(null=True,max_length=200)
    author = models.ForeignKey(Author,on_delete = models.CASCADE,null=True)
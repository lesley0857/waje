from django.contrib import admin

from wajeapp.models import Book
from .models import *

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
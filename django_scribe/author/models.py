from django.db import models
# from Books.models import Book
# Create your models here.

class Author(models.Model):
    Name = models.CharField(max_length=120)
    # books = models.Model(Book)
    contact = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank= True)
from django.db import models
# from Books.models import Book
# Create your models here.

class Author(models.Model):
    # books = models.ForeignKey(Book.objects.filter(Author = Self.__name__), null= False, on_delete= models.DO_NOTHING)

    name = models.CharField(max_length=120)
    contact = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank= True)
    photo = models.ImageField(null= True, blank=True)

    def __str__(self) -> str:
        return self.name
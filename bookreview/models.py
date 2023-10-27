from django.db import models
from main.models import TakugoUser
from books.models import Book
# Create your models here.

class BookReview(models.Model):
    comment = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(TakugoUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now=True)

from django.db import models

from books.models import Book
from main.models import TakugoUser

class BookJournal(models.Model):
    user = models.ForeignKey(TakugoUser, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE) # harusnya many to many????

    notes = models.TextField()
    favorite_quotes = models.TextField()
    rating = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

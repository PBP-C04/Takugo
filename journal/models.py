from django.db import models
from django.utils import timezone

from books.models import Book
from main.models import TakugoUser

class BookJournal(models.Model):
    user = models.ForeignKey(TakugoUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    notes = models.TextField()
    favorite_quotes = models.TextField()
    rating = models.IntegerField()
    date_started = models.DateField(default=timezone.now)
    date_finished = models.DateField(default=timezone.now)
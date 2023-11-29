from django.db import models

# Create your models here.

from main.models import TakugoUser
from books.models import Book

class BookDonate(models.Model):
    donatur = models.ForeignKey(TakugoUser, on_delete=models.CASCADE, related_name='donatur')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    lembaga = models.ForeignKey(TakugoUser, on_delete=models.CASCADE, related_name='lembaga')
    kondisi = models.CharField(max_length=100)
    tanggal_donasi = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(TakugoUser, on_delete=models.CASCADE, related_name='user')
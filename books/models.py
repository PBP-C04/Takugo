from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from main.models import TakugoUser

# Create your models here.
class Book(models.Model):
    BOOK_TYPES = [
        ("MGA", "Manga"),
        ("LNV", "Light-Novel"),
        ("DJS", "Doujinshi"),
        ("MHW", "Manhwa"),
        ("MHU", "Manhua"),
        ("NVL", "Novel"),
        ("OTH", "Other"),
    ]

    title = models.CharField(max_length=100)
    book_type = models.CharField(max_length=3, choices=BOOK_TYPES)
    volumes = models.SmallIntegerField(
        default=1, 
        validators=[MinValueValidator(1, "Book has to have at least 1 volume")]
    )
    image_url = models.URLField()
    score = models.FloatField(
        default=0.0, 
        validators=[
            MinValueValidator(0.0, "Score cannot be lower than 0"),
            MaxValueValidator(10.0, "Maximum score of a book is 10"),
        ]
    )


class BoughtBook(models.Model):
    user = models.ForeignKey(TakugoUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    amount = models.SmallIntegerField(
        default=1, 
        validators=[
            MinValueValidator(1, "Amount cannot be lower than 1"), 
            MaxValueValidator(20, "Maximum amount of books to buy is 20"),
        ]
    )

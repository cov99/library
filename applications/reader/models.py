from django.db import models
from applications.book.models import Book
from .managers import ReaderManager

class Reader(models.Model):
    names = models.CharField(
        max_length=50
    )
    surnames = models.CharField(
        max_length=50
    )
    nationality = models.CharField(
        max_length=30
    )
    age = models.PositiveIntegerField(default=0)

    objects = ReaderManager()

    def __str__(self):
        return self.names


class LendLease(models.Model):
    reader = models.ForeignKey(
        Reader,
        on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )
    loan_date = models.DateField()
    return_date = models.DateField(
        blank=True,
        null=True,
    ) #campo no obligatorio
    returned = models.BooleanField()

    def __str__(self):
        return self.book.tittle

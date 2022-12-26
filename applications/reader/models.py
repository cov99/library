from django.db import models
from applications.book.models import Book
from applications.author.models import Person
from .managers import LendleaseManager

class Reader(Person):
    
    class Meta:
        verbose_name = 'Reader'
        verbose_name_plural = 'Readers'

class LendLease(models.Model):
    reader = models.ForeignKey(
        Reader,
        on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='book_lendlease',
    )
    loan_date = models.DateField()
    return_date = models.DateField(
        blank=True,
        null=True,
    ) #campo no obligatorio
    returned = models.BooleanField()
    objects = LendleaseManager()

    def save(self, *args, **kwargs):

        print('========')
        self.book.stock = self.book.stock -1
        self.book.save()

        super(LendLease, self).save(*args, **kwargs)

    def __str__(self):
        return self.book.tittle

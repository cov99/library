from django.db import models
# managers
from .managers import AuthorManager


class Person(models.Model):
    names = models.CharField(
        max_length=50
    )
    surnames = models.CharField(
        max_length=50
    )
    nationality = models.CharField(
        max_length=20
    )
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.id} - {self.names} - {self.surnames}"
    
    class Meta:
        abstract = True


class Author(Person):
    pseudonym = models.CharField(
        'seudonimo',
        max_length=50,
        blank=True
    )
    objects = AuthorManager()

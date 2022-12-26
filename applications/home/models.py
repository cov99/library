from django.db import models
from .managers import PersonManager

class Person(models.Model):
    full_name = models.CharField('Nombres', max_length=50)
    country = models.CharField('Pais', max_length=30)
    passport = models.CharField('Pasaporte', max_length=30)
    age = models.PositiveIntegerField()
    appellative = models.CharField('Apelativo', max_length=10)

    objects = PersonManager()

    class Meta:
        """Meta definition for Person."""

        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
        db_table = 'person'
        unique_together = ['age', 'appellative']
        constraints = [
            models.CheckConstraint(
                check=models.Q(age__gte=18),
                name='age_older_18',
            )
        ]
        abstract = True

    def __str__(self):
        """Unicode representation of Person"""
        return self.full_name

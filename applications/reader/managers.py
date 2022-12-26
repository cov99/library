import datetime
from django.db import models
from django.db.models import Count, Avg, Sum
from django.db.models.functions import Lower

class LendleaseManager(models.Manager):
    """loan procedures"""

    def books_average_ages(self):
        result = self.filter(
            book__id='2'
        ).aggregate(
            average_age=Avg('reader__age'),
            addition_age=Sum('reader__age'),
        )
        return result
    
    def num_borroweds_books(self):
        result = self.values(
            'book'
        ).annotate(
            num_borroweds=Count('book'),
            tittle=Lower('book__tittle'),
        )

        for r in result:
            print('=======')
            print(r, r['num_borroweds'])

        return result

import datetime
from django.db import models
from django.db.models import Q


class BookManager(models.Manager):
    """ managers for the book model"""

    def list_books(self, kword):

        result = self.filter(
            tittle__icontains=kword,
            release_date__range=('2000-01-01', '2010-01-01')
        )

        return result

    def list_books2(self, kword, release_date1, release_date2):

        date1 = datetime.datetime.strptime(release_date1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(release_date2, "%Y-%m-%d").date()

        result = self.filter(
            tittle__icontains=kword,
            release_date__range=(date1, date2)
        )

        return result
    
    def list_books_category(self, category):

        return self.filter(
            category__id=category
        ).order_by('tittle')

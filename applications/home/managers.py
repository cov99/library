import datetime
from django.db import models
from django.db.models import Count

class PersonManager(models.Manager):
    """ managers for the book model"""

    def list_person(self):
        result = self.annotate(
            num_persons=Count('person')
        )
        for r in result:
            print('*******')
            print(r, r.num_persons)
        return result

from django.db import models
from django.db.models import Q


class AuthorManager(models.Manager):
    """ managers for the author model"""

    def search_author(self, kword):

        result = self.filter(
            name__icontains=kword
        )

        return result

    def search_author2(self, kword):

        result = self.filter(
            Q(name__icontains=kword) | Q(surnames__icontains=kword)
        )

        return result
    
    def search_author3(self, kword):

        result = self.filter(
            name__icontains=kword
        ).exclude(
            Q(age__icontains=35) | Q(age__icontains=69)
        )

        return result
    
    def search_author4(self, kword):

        result = self.filter(
            age__gt=40,
            age__lt=65
        ).order_by('surnames', 'name')

        return result

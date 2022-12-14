from django.db import models
from django.db.models import Q

class ReaderManager(models.Manager):
    """ managers for the reader model"""

    def list_readers(self, kword):

        result = self.filter(
            names__icontains=kword
        )

        return result

    def list_readers2(self, kword):

        result = self.filter(
            Q(name__icontains=kword) | Q(surnames__icontains=kword)
        )

        return result
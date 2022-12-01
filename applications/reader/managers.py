from django.db import models

class ReaderManager(models.Manager):
    """ managers for the reader model"""

    def list_reader(self):
        return self.all()

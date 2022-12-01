from django.db import models

class AuthorManager(models.Manager):
    """ managers for the author model"""

    def list_authors(self):
        return self.all()
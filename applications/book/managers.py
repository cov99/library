from django.db import models

class BookManager(models.Manager):
    """ managers for the book model"""

    def list_books(self):
        return self.all()

class CategoryManager(models.Manager):

    def list_categories(self):
        return self.all()

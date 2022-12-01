from django.db import models
from applications.author.models import Author

class Category(models.Model):
    name = models.CharField(
        max_length=30
    )

    def __str__(self):
        return self.name

class Book(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    authors = models.ManyToManyField(Author)
    tittle = models.CharField(
        max_length=50
    )
    release_date = models.DateField()
    front_page = models.ImageField(upload_to='front_page')
    visits = models.PositiveIntegerField()

    def __str__(self):
        return self.tittle

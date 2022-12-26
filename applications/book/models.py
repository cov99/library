from django.db import models
from applications.author.models import Author
# managers
from .managers import BookManager, CategoryManager

class Category(models.Model):
    name = models.CharField(
        max_length=30
    )
    objects = CategoryManager()

    def __str__(self):
        return f"{str(self.id)} - {str(self.name)}"

class Book(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category_book'
    )
    authors = models.ManyToManyField(Author)
    tittle = models.CharField(
        max_length=50
    )
    release_date = models.DateField()
    front_page = models.ImageField(upload_to='front_page')
    visits = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)

    objects = BookManager()

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
        ordering = ['tittle', 'release_date']

    def __str__(self):
        return f"{str(self.id)} - {self.tittle}"

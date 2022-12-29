from django.db import models
from django.db.models.signals import post_save
# apps terceros
from PIL import Image
# from local apps
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

def optimize_image(sender, instance, **kwargs):
    print(" ======== ")
    if instance.front_page:
        front_page = Image.open(instance.front_page.path)
        front_page.save(instance.front_page.path, quality=20, optimize=True)


post_save.connect(optimize_image, sender=Book)

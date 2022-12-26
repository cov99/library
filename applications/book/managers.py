import datetime
from django.db import models
from django.db.models import Count
from django.contrib.postgres.search import TrigramSimilarity

class BookManager(models.Manager):
    """ managers for the book model"""

    def list_books(self, kword):

        result = self.filter(
            tittle__icontains=kword,
            release_date__range=('2000-01-01', '2010-01-01')
        )

        return result
    
    def list_books_trgm(self, kword):
        
        if kword:
            result = self.filter(
                tittle__trigram_similar=kword,
            )
            return result
        else:
            return self.all()[:10]

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
    
    def add_author_book(self, book_id, author):
        book = self.get(id=book_id)
        book.authors.add(author)
        return book
    
    def books_num_lendlease(self):
        result = self.aggregate(
            num_lendlease=Count('book_lendlease')
        )
        return result
    
    def num_borrowed_books(self):
        result = self.annotate(
            num_borroweds=Count('book_lendlease')
        )

        for r in result:
            print('=======')
            print(r, r.num_borroweds)

        return result


class CategoryManager(models.Manager):
    """ managers for the book model"""

    def category_for_author(self, author):
        return self.filter(
            category_book__authors__id=author
        ).distinct() #para que la categoria no se repita
    
    def list_category_books(self):
        result = self.annotate(
            num_books=Count('category_book')
        )
        for r in result:
            print('*******')
            print(r, r.num_books)
        return result

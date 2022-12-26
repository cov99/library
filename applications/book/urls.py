from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(
        'books/',
        views.ListBooks.as_view(),
        name="books"
    ),
    path(
        'books-2/',
        views.ListBooks2.as_view(),
        name="books2"
    ),
    path(
        'books-trg/',
        views.ListBooksTrg.as_view(),
        name="books-trg"
    ),
    path(
        'book-detail/<pk>',
        views.BookDetailView.as_view(),
        name="book-detail"
    ),
]

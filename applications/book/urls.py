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
]

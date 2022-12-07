from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

class ListBooks(ListView):
    context_object_name = 'list_books'
    template_name = 'book/list.html'

    def get_queryset(self):

        return Book.objects.list_books()

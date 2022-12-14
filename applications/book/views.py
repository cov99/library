from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

class ListBooks(ListView):
    context_object_name = 'list_books'
    template_name = 'book/list.html'

    def get_queryset(self):
        keyword = self.request.GET.get("kword", None)
        if keyword:
            return Book.objects.list_books(keyword)
        # release_date1
        rd1 = self.request.GET.get("release_date1", None)
        if rd1:
            return Book.objects.list_books(keyword)
        # release_date2
        rd2 = self.request.GET.get("release_date2", None)
        if rd2:
            return Book.objects.list_books2(keyword, rd1, rd2)

        return Book.objects.all()


class ListBooks2(ListView):
    context_object_name = 'list_books'
    template_name = 'book/list2.html'

    def get_queryset(self):

        return Book.objects.list_books_category('5')

from django.shortcuts import render
from django.views.generic import ListView
from .models import Author

class ListAuthors(ListView):
    context_object_name = 'list_authors'
    template_name = 'author/list.html'

    def get_queryset(self):
        keyword = self.request.GET.get("kword", None)
        if keyword:
            return Author.objects.search_author4(keyword)
        return Author.objects.all()

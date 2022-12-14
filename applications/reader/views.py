from django.shortcuts import render
from django.views.generic import ListView
from .models import Reader, LendLease

class ListReaders(ListView):
    context_object_name = 'list_readers'
    template_name = 'reader/list.html'

    def get_queryset(self):
        keyword = self.request.GET.get("kword", None)
        if keyword:
            return Reader.objects.list_readers(keyword)
        return Reader.objects.all()

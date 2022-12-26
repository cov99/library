from django.shortcuts import render
from django.views.generic import ListView
from .models import Person

class ListPerson(ListView):
    context_object_name = 'list_person'
    template_name = 'person/list.html'

    def get_queryset(self):
        keyword = self.request.GET.get("kword", None)
        if keyword:
            return Person.objects.list_person(keyword)
        return Person.objects.all()


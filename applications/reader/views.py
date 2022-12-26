from datetime import date
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from .models import LendLease
from .forms import LendLeaseForm, MultipleLendLeaseForm


class LendLeaseRegistration(FormView):
    template_name = 'reader/add_lendlease.html'
    form_class = LendLeaseForm
    success_url = '.'

    def form_valid(self, form):

        # LendLease.objects.create(
        #    reader=form.cleaned_data['reader'],
        #    book=form.cleaned_data['book'],
        #    loan_date=date.today(),
        #    returned=False
        # )

        lendlease = LendLease(
            reader=form.cleaned_data['reader'],
            book=form.cleaned_data['book'],
            loan_date=date.today(),
            returned=False
        )
        lendlease.save()

        book = form.cleaned_data['book']
        book.stock = book.stock -1
        book.save() #actualizamos el dato que ya existe

        return super(LendLeaseRegistration, self).form_valid(form)


class AddLendLease(FormView):
    template_name = 'reader/add_lendlease.html'
    form_class = LendLeaseForm
    success_url = '.'

    def form_valid(self, form):

        obj, created = LendLease.objects.get_or_create(
            reader=form.cleaned_data['reader'],
            book=form.cleaned_data['book'],
            returned = False,
            defaults={
                'loan_date': date.today()
            }
        )

        if created:
            return super(AddLendLease, self).form_valid(form)
        else:
            return HttpResponseRedirect('/')


class AddMultipleLendLease(FormView):
    template_name = 'reader/add_multiple_lendlease.html'
    form_class = MultipleLendLeaseForm
    success_url = '.'

    def form_valid(self, form):

        

        return super(AddMultipleLendLease, self).form_valid(form)
from django import forms
from applications.book.models import Book
from .models import LendLease

class LendLeaseForm(forms.ModelForm):

    class Meta:
        model = LendLease
        fields = (
            'reader',
            'book',
        )


class MultipleLendLeaseForm(forms.ModelForm):

    books = forms.ModelMultipleChoiceField(
        queryset=None,
        required=True,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = LendLease
        fields = (
            'reader',
        )
    
    def __init__(self, *args, **kwargs):
        super(MultipleLendLeaseForm, self).__init__(*args, **kwargs)
        self.fields['books'].queryset = Book.objects.all()

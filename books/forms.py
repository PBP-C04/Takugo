from django import forms
from django.forms import ModelForm

from books.models import BoughtBook


class BookForm(ModelForm):
    amount = forms.IntegerField(min_value=1, max_value=20)

    class Meta:
        model = BoughtBook
        fields = ["amount"]

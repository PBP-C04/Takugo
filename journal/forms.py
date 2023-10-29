from django import forms
from journal.models import BookJournal
from django.forms import ModelForm

class BookJournalForm(forms.ModelForm):
    notes = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Write your thoughts...', 'class': "form-control"}),
        required=True,
        error_messages={'required': 'This field is required'}  # Pesan error jika field dibiarkan kosong
    )
    favorite_quotes = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Write your favorite quotes...', 'class': "form-control"}),
        required=True,
        error_messages={'required': 'This field is required'}  # Pesan error jika field dibiarkan kosong
    )
    rating = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 1, 'max': 5, 'value': 1, 'class': "form-control"}),
        required=True,
        error_messages={'required': 'This field is required'}  # Pesan error jika field dibiarkan kosong
    )

    class Meta:
        model = BookJournal
        fields = ["notes", "favorite_quotes", "rating"]

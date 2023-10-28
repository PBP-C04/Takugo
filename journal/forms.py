from django import forms
from django.utils import timezone
from journal.models import BookJournal  # Pastikan model BookJournal sudah diimport
from django.forms import ModelForm

class BookJournalForm(forms.ModelForm):  # Ganti nama kelas menjadi BookJournalForm
    notes = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your thoughts...'}), required=True)  # Gunakan CharField dan widget Textarea
    favorite_quotes = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your favorite quotes...'}), required=True)  # Gunakan CharField dan widget Textarea
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'type': 'range', 'min': 1, 'max': 5, 'value': 1}), required=True)
    date_started = forms.DateField()
    date_finished = forms.DateField()

    class Meta:
        model = BookJournal
        fields = ["notes", "favorite_quotes", "rating", "date_started", "date_finished"]
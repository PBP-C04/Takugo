from django.forms import ModelForm
from bookreview.models import BookReview
from django import forms

class BookReviewForm(ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Tell us more about this book...', 'class': 'form-control', 'rows': 4}),
        required=True
    )
    rating = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 1, 'max': 5, 'value': 1, 'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = BookReview
        fields = ['comment', 'rating']

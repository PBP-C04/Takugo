from django.forms import ModelForm
from bookreview.models import BookReview
from django import forms

class BookReviewForm(ModelForm):
    comment = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'give your comment here...'}), required=True)
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'type': 'range', 'min': 1, 'max': 5}), required=True)
    class Meta:
        model = BookReview
        fields = ['comment', 'rating']
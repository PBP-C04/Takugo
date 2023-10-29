from django.forms import ModelForm
from donate.models import *

class DonateForm(ModelForm):
    class Meta:
        model = BookDonate
        fields = ['kondisi']
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from main.models import TakugoUser


class RegisterForm(UserCreationForm):
    TYPES = [("U", "Regular User"), ("I", "Institution")]
    user_type = forms.ChoiceField(required=True, choices=TYPES)

    class Meta(UserCreationForm.Meta):
        model = TakugoUser
        fields = UserCreationForm.Meta.fields + ("user_type",)


class ChangeForm(UserChangeForm):
    TYPES = [("U", "Regular User"), ("I", "Institution")]
    user_type = forms.ChoiceField(required=True, choices=TYPES)

    class Meta(UserCreationForm.Meta):
        model = TakugoUser
        fields = UserCreationForm.Meta.fields + ("user_type",)

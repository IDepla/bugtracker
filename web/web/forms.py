from django import forms
from .models import User, Bug


class UserUpdateNameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class PaginatorForm(forms.Form):

    page = forms.IntegerField(min_value=1, max_value=100000)

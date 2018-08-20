from django import forms


class RialIncForm(forms.Form):
    amount = forms.IntegerField(required=True, min_value=1000, initial=0)

from django import forms


class RialIncForm(forms.Form):
    amount = forms.IntegerField(required=True, min_value=1000, initial=0)


class ExchangeForm(forms.Form):
    amount = forms.IntegerField()
    CHOICES = (('dollar', 'Dollar'),
               ('euro', 'Euro'))
    picked = forms.MultipleChoiceField(choices=CHOICES, widget=forms.MultipleChoiceField())

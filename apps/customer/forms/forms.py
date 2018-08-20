from django import forms


class RialIncForm(forms.Form):
    amount = forms.IntegerField(required=True, min_value=1000, initial=0)


class ExchangeForm(forms.Form):
    amount = forms.IntegerField( required=True, min_value=10, initial=0)
    CHOICES = (('dollar', 'Dollar'),
               ('euro', 'Euro'))
    currency = forms.MultipleChoiceField(choices=CHOICES, label='currency',)



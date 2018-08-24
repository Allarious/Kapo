from apps.transactions.models import *
from django import forms


class ExamTransactionForm(forms.ModelForm):
    class Meta:
        model = ExamTransaction
        fields = ['exam_title', 'dollar_cost', 'site_url', 'site_authentication', 'site_username', 'site_password',
                  'description']


class ApplicationTuitionFeeTransactionForm(forms.ModelForm):
    class Meta:
        model = ApplicationTuitionFeeTransaction
        fields = ['fee_type', 'dollar_cost', 'euro_cost', 'site_url', 'site_authentication', 'site_username',
                  'site_password', 'description']


class ForeignPaymentTransactionForm(forms.ModelForm):
    foreign_card_number = CreditCardField(placeholder=u'0000 0000 0000 0000', min_length=12, max_length=19)

    class Meta:
        model = ForeignPaymentTransaction
        fields = ['foreign_card_number', 'dollar_cost', 'euro_cost', 'description']


class DomesticPaymentTransactionForm(forms.ModelForm):
    domestic_card_number = forms.CharField(min_length=16, max_length=16)

    class Meta:
        model = DomesticPaymentTransaction
        fields = ['domestic_card_number', 'rial_cost', 'description']


class UnknownPaymentTransactionForm(forms.ModelForm):
    class Meta:
        model = UnknownPaymentTransaction
        fields = ['domestic_card_number', 'rial_cost', 'description']

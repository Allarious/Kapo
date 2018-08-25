from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from apps.accounts.models import MyUser
from apps.customer.models import Customer, DomesticCardField

from django import forms
from django.forms.widgets import TextInput
from django.utils.translation import ugettext_lazy as _

from apps.employee.models import Employee


class TelephoneInput(TextInput):
    # switch input type to type tel so that the numeric keyboard shows on mobile devices
    input_type = 'tel'


class CreditCardField(forms.CharField):
    # validates almost all of the example cards from PayPal
    # https://www.paypalobjects.com/en_US/vhelp/paypalmanager_help/credit_card_numbers.htm
    cards = [
        {
            'type': 'maestro',
            'patterns': [5018, 502, 503, 506, 56, 58, 639, 6220, 67],
            'length': [12, 13, 14, 15, 16, 17, 18, 19],
            'cvvLength': [3],
            'luhn': True
        }, {
            'type': 'forbrugsforeningen',
            'patterns': [600],
            'length': [16],
            'cvvLength': [3],
            'luhn': True
        }, {
            'type': 'dankort',
            'patterns': [5019],
            'length': [16],
            'cvvLength': [3],
            'luhn': True
        }, {
            'type': 'visa',
            'patterns': [4],
            'length': [13, 16],
            'cvvLength': [3],
            'luhn': True
        }, {
            'type': 'mastercard',
            'patterns': [51, 52, 53, 54, 55, 22, 23, 24, 25, 26, 27],
            'length': [16],
            'cvvLength': [3],
            'luhn': True
        }, {
            'type': 'amex',
            'patterns': [34, 37],
            'length': [15],
            'cvvLength': [3, 4],
            'luhn': True
        }, {
            'type': 'dinersclub',
            'patterns': [30, 36, 38, 39],
            'length': [14],
            'cvvLength': [3],
            'luhn': True
        }, {
            'type': 'discover',
            'patterns': [60, 64, 65, 622],
            'length': [16],
            'cvvLength': [3],
            'luhn': True
        }, {
            'type': 'unionpay',
            'patterns': [62, 88],
            'length': [16, 17, 18, 19],
            'cvvLength': [3],
            'luhn': False
        }, {
            'type': 'jcb',
            'patterns': [35],
            'length': [16],
            'cvvLength': [3],
            'luhn': True
        }
    ]

    def __init__(self, placeholder=None, *args, **kwargs):
        super(CreditCardField, self).__init__(
            # override default widget
            widget=TelephoneInput(attrs={
                'placeholder': placeholder
            })
            , *args, **kwargs)

    default_error_messages = {
        'invalid': _(u'The credit card number is invalid'),
    }

    def clean(self, value):

        # ensure no spaces or dashes
        value = value.replace(' ', '').replace('-', '')

        # get the card type and its specs
        card = self.card_from_number(value)

        # if no card found, invalid
        if not card:
            raise forms.ValidationError(self.error_messages['invalid'])

        # check the length
        if not len(value) in card['length']:
            raise forms.ValidationError(self.error_messages['invalid'])

        # test luhn if necessary
        if card['luhn']:
            if not self.validate_mod10(value):
                raise forms.ValidationError(self.error_messages['invalid'])

        return value

    def card_from_number(self, num):
        # find this card, based on the card number, in the defined set of cards
        for card in self.cards:
            for pattern in card['patterns']:
                if (str(pattern) == str(num)[:len(str(pattern))]):
                    return card

    def validate_mod10(self, num):
        # validate card number using the Luhn (mod 10) algorithm
        checksum, factor = 0, 1
        for c in reversed(num):
            for c in str(factor * int(c)):
                checksum += int(c)
            factor = 3 - factor
        return checksum % 10 == 0


class AbstractTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(default=timezone.now)
    description = models.TextField(null=True, blank=True)
    paid = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    checking_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    checking = models.BooleanField(default=False)

    class Meta:
        abstract = True


class RialWalletIncTransaction(AbstractTransaction):
    amount = models.FloatField(default=0, validators=[MaxValueValidator(300000000), MinValueValidator(100000)])

    def __str__(self):
        return 'Rial inc ' + str(self.id)


class CurrencyConvertTransaction(AbstractTransaction):
    rial_cost = models.FloatField(validators=[MaxValueValidator(300000000), MinValueValidator(100000)])
    CHOICES = (('dollar', 'Dollar'), ('euro', 'Euro'))
    currency = models.CharField(choices=CHOICES, max_length=20)
    amount = models.FloatField(validators=[MaxValueValidator(1000), MinValueValidator(1)])

    def __str__(self):
        return str(self.currency) + ' Convert ' + str(self.id)


class ExamTransaction(AbstractTransaction):
    exam_title = models.CharField(max_length=30)
    dollar_cost = models.FloatField(default=0, validators=[MaxValueValidator(1000), MinValueValidator(1)])
    site_url = models.URLField(null=True, blank=True)
    site_authentication = models.NullBooleanField(default=False)
    site_username = models.CharField(null=True, blank=True, max_length=50)
    site_password = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.exam_title + ' ' + str(self.id)


class ApplicationTuitionFeeTransaction(AbstractTransaction):
    FEE_CHOICES = (('application fee', 'Application Fee'), ('tuition fee', 'Tuition Fee'))
    fee_type = models.CharField(choices=FEE_CHOICES, max_length=50)

    dollar_cost = models.FloatField(default=0,
                                    null=True, blank=True,
                                    validators=[MaxValueValidator(1000), MinValueValidator(0)])

    euro_cost = models.FloatField(default=0,
                                  null=True, blank=True,
                                  validators=[MaxValueValidator(1000), MinValueValidator(0)])

    site_url = models.URLField(null=True, blank=True)
    site_authentication = models.BooleanField(default=False)
    site_username = models.CharField(null=True, blank=True, max_length=50)
    site_password = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.fee_type + ' ' + str(self.id)


class ForeignPaymentTransaction(AbstractTransaction):
    dollar_cost = models.FloatField(default=0,
                                    null=True, blank=True,
                                    validators=[MaxValueValidator(1000), MinValueValidator(0)])

    euro_cost = models.FloatField(default=0,
                                  null=True, blank=True,
                                  validators=[MaxValueValidator(1000), MinValueValidator(0)])

    foreign_card_number = models.CharField(max_length=19)

    def __str__(self):
        return 'Foreign payment ' + str(self.id)


class DomesticPaymentTransaction(AbstractTransaction):
    rial_cost = models.FloatField(default=0, validators=[MaxValueValidator(30000000), MinValueValidator(10000)])
    domestic_card_number = DomesticCardField(max_length=16)

    def __str__(self):
        return 'Domestic payment' + ' ' + str(self.id)


class UnknownPaymentTransaction(AbstractTransaction):
    rial_cost = models.FloatField(default=0, validators=[MaxValueValidator(30000000), MinValueValidator(10000)])
    domestic_card_number = models.CharField(max_length=16)

    def __str__(self):
        return 'Unknown payment' + ' ' + str(self.id)

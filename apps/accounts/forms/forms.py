from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.forms.models import ModelForm
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import ugettext_lazy as _
from apps.accounts.models import MyUser
from apps.customer.models import Customer
from apps.accounts.tokens import account_activation_token
from captcha.fields import ReCaptchaField

from apps.employee.models import Employee


class UserForm1(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'email', 'password2')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        confirm_password = cleaned_data.get('password2')
        password = cleaned_data.get('password')
        if not password == confirm_password:
            raise forms.ValidationError('Password does not match.')


# TODO injam fieldaye model ezafe beshan
class CustomerSignUpForm(forms.ModelForm):
    terms = forms.BooleanField(required=True)

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'birthday_date', 'city', 'country',
                  'phone')  # , 'gender', 'day', 'month', 'year', 'national_id', 'city', 'address', 'phone')


class EmployeeSignUpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name')

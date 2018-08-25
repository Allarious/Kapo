from django import forms
from apps.employee.models import Employee
from apps.accounts.models import MyUser, SEX_CHOICES
from datetime import date


class EditEmployeeProfile(forms.ModelForm):
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)
    # gender = forms.CharField(max_length=10, choices=SEX_CHOICES, default='male')
    birthday_date = forms.DateField(required=False)
    # national_id = forms.CharField(max_length=10, default='')
    city = forms.CharField(max_length=10, required=False)
    country = forms.CharField(max_length=20, required=False)
    # address = forms.CharField(max_length=100, default='Tehran')
    phone = forms.CharField(max_length=12, required=False)

    # domestic_bank_account_id = forms.CharField(unique=False, max_length=16, null=True)

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'birthday_date', 'city', 'country', 'phone')
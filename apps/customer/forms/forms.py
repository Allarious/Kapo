from django import forms
from apps.customer.models import Customer
from apps.accounts.models import MyUser, SEX_CHOICES
from datetime import date


class EditUser(forms.ModelForm):
    username = forms.CharField(max_length=30, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(widget=forms.PasswordInput, required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'email', 'password2')

    def clean(self):
        cleaned_data = super(EditUser, self).clean()
        confirm_password = cleaned_data.get('password2')
        password = cleaned_data.get('password')
        if not password == confirm_password and password != '':
            raise forms.ValidationError('Password does not match.')


class EditCustomerProfile(forms.ModelForm):
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
        model = Customer
        fields = ('first_name', 'last_name', 'birthday_date', 'city', 'country', 'phone')

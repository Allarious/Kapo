# Generated by Django 2.0 on 2018-08-25 07:33

import apps.customer.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Non Binary')], default='male', max_length=10)),
                ('birthday_date', models.DateField(default=datetime.date.today)),
                ('national_id', models.CharField(default='', max_length=10)),
                ('city', models.CharField(default='', max_length=10)),
                ('country', models.CharField(default='Iran', max_length=20)),
                ('address', models.CharField(default='Tehran', max_length=100)),
                ('phone', models.CharField(default='', max_length=12)),
                ('domestic_card_number', apps.customer.models.DomesticCardField(max_length=16, null=True)),
                ('rial_wallet', models.FloatField(default=0)),
                ('dollar_wallet', models.FloatField(default=0)),
                ('euro_wallet', models.FloatField(default=0)),
            ],
        ),
    ]

# Generated by Django 2.0 on 2018-08-24 12:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20180824_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birthday_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

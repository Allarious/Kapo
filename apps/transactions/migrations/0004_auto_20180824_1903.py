# Generated by Django 2.0 on 2018-08-24 19:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_auto_20180824_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationtuitionfeetransaction',
            name='dollar_cost',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='applicationtuitionfeetransaction',
            name='euro_cost',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='foreignpaymenttransaction',
            name='dollar_cost',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='foreignpaymenttransaction',
            name='euro_cost',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)]),
        ),
    ]

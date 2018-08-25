# Generated by Django 2.0 on 2018-08-25 06:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20180825_0401'),
        ('transactions', '0006_auto_20180825_0542'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyConvertTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('rial_cost', models.FloatField(validators=[django.core.validators.MaxValueValidator(300000000), django.core.validators.MinValueValidator(100000)])),
                ('currency', models.CharField(choices=[('dollar', 'Dollar'), ('euro', 'Euro')], max_length=20)),
                ('amount', models.FloatField(validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RialWalletIncTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('amount', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(300000000), django.core.validators.MinValueValidator(100000)])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 2.0 on 2018-08-24 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='dollar_wallet',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='euro_wallet',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='rial_wallet',
            field=models.FloatField(default=0),
        ),
    ]
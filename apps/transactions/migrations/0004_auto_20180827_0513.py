# Generated by Django 2.0 on 2018-08-27 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_auto_20180826_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationtuitionfeetransaction',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='currencyconverttransaction',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='domesticpaymenttransaction',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='examtransaction',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='foreignpaymenttransaction',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='rialwalletinctransaction',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='unknownpaymenttransaction',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

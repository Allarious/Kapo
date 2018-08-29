# Generated by Django 2.0 on 2018-08-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0009_rialwalletinctransaction_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationtuitionfeetransaction',
            name='type_name',
            field=models.CharField(default='no name', max_length=50),
        ),
        migrations.AlterField(
            model_name='currencyconverttransaction',
            name='type_name',
            field=models.CharField(default='no name', max_length=50),
        ),
        migrations.AlterField(
            model_name='domesticpaymenttransaction',
            name='type_name',
            field=models.CharField(default='no name', max_length=50),
        ),
        migrations.AlterField(
            model_name='examtransaction',
            name='type_name',
            field=models.CharField(default='no name', max_length=50),
        ),
        migrations.AlterField(
            model_name='foreignpaymenttransaction',
            name='type_name',
            field=models.CharField(default='no name', max_length=50),
        ),
        migrations.AlterField(
            model_name='rialwalletinctransaction',
            name='type_name',
            field=models.CharField(default='no name', max_length=50),
        ),
        migrations.AlterField(
            model_name='unknownpaymenttransaction',
            name='type_name',
            field=models.CharField(default='no name', max_length=50),
        ),
    ]
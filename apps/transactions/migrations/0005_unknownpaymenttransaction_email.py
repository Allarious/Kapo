# Generated by Django 2.0 on 2018-08-27 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_auto_20180827_0513'),
    ]

    operations = [
        migrations.AddField(
            model_name='unknownpaymenttransaction',
            name='email',
            field=models.EmailField(default='hazrat@gmail.com', max_length=254),
        ),
    ]
# Generated by Django 2.0 on 2018-08-26 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_systemaccounts'),
        ('manager', '0002_auto_20180826_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='system_accounts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SystemAccounts'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Non Binary')], default='female', max_length=10),
        ),
    ]

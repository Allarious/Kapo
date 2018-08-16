# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-08-16 22:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_manager', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True, verbose_name='Mobile number\u200c')),
                ('organization', models.CharField(max_length=128, verbose_name='Organization\u200c')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Age\u200c')),
                ('national_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='National code\u200c')),
                ('tel_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telephone number\u200c')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True, verbose_name='Mobile number\u200c')),
                ('organization', models.CharField(max_length=128, verbose_name='Organization\u200c')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Age\u200c')),
                ('national_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='National code\u200c')),
                ('tel_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telephone number\u200c')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]

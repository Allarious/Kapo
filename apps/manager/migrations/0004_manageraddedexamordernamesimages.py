# Generated by Django 2.0 on 2018-08-26 22:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20180826_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerAddedExamOrderNamesImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_title', models.CharField(max_length=30)),
                ('dollar_cost', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)])),
                ('site_url', models.URLField(blank=True, null=True)),
                ('image_url', models.URLField()),
            ],
        ),
    ]
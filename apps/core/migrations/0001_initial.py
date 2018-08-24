# Generated by Django 2.0 on 2018-08-24 10:12

import apps.customer.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationTuitionFeeTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('fee_type', models.CharField(choices=[('application fee', 'Application Fee'), ('tuition fee', 'Tuition Fee')], max_length=50)),
                ('dollar_cost', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)])),
                ('euro_cost', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)])),
                ('site_url', models.URLField(blank=True, null=True)),
                ('site_authentication', models.BooleanField(default=False)),
                ('site_username', models.CharField(blank=True, max_length=50, null=True)),
                ('site_password', models.CharField(blank=True, max_length=50, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=10)),
                ('value', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DomesticPaymentTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('rial_cost', models.IntegerField(validators=[django.core.validators.MaxValueValidator(30000000), django.core.validators.MinValueValidator(10000)])),
                ('domestic_card_number', apps.customer.models.DomesticCardField(max_length=16)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExamTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('exam_title', models.CharField(max_length=30)),
                ('dollar_cost', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)])),
                ('site_url', models.URLField(blank=True, null=True)),
                ('site_authentication', models.BooleanField(default=False)),
                ('site_username', models.CharField(blank=True, max_length=50, null=True)),
                ('site_password', models.CharField(blank=True, max_length=50, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ForeignPaymentTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('dollar_cost', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)])),
                ('euro_cost', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)])),
                ('foreign_card_number', models.CharField(max_length=19)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UnknownPaymentTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('rial_cost', models.IntegerField(validators=[django.core.validators.MaxValueValidator(30000000), django.core.validators.MinValueValidator(10000)])),
                ('domestic_card_number', models.CharField(max_length=16)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

from django.db import models


class Configuration(models.Model):
    key = models.CharField(max_length=20)
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.key


class SystemAccounts(models.Model):
    rial_amount_account = models.FloatField(default=0)
    dollar_amount_account = models.FloatField(default=0)
    euro_amount_account = models.FloatField(default=0)

from django.db import models


class Configuration(models.Model):
    key = models.CharField(max_length=10)
    value = models.CharField(max_length=10)

    def __str__(self):
        return self.key

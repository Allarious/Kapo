from django.db import models


class Configuration(models.Model):
    key = models.CharField(max_length=20)
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.key

from django.db import models

class Records(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

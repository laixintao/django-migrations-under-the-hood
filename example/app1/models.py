from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    intc = models.IntegerField()
    intd = models.IntegerField()

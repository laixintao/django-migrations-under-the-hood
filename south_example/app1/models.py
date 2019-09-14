from django.db import models

class Knight(models.Model):
    name = models.CharField(max_length=100)
    of_the_round_table = models.BooleanField()

# Create your models here.
from django.db import models

class Currency(models.Model):
	currency_code = models.CharField(max_length=5)
	value = models.CharField(max_length=10, default='0.0')
	published_date = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.currency_code



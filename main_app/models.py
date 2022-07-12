from django.db import models
from django.urls import reverse

# Create your models here.

class Exchange(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("exchange_detail", kwargs={"exchange_id": self.id})
    
class Wallet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wallet_detail", kwargs={"wallet_id": self.id})
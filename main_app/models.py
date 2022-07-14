from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Exchange(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("exchange_detail", kwargs={"pk": self.id})
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Wallet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wallet_detail", kwargs={"pk": self.id})

    user = models.ForeignKey(User, on_delete=models.CASCADE)
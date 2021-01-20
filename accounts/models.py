from django.db import models
from django.contrib.auth.models import User


class Bio(models.Model):
    firstname = models.CharField(max_length=30)
    secondname = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', default='images/home-profile.jpg')
    phone = models.IntegerField()
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Billing(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)
    num = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    postal = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

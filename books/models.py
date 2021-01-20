from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    image = models.ImageField(default='images/home-profile.jpg')
    category = models.CharField(max_length=50)
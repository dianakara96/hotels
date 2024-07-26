# models.py
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.name

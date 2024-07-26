# models.py
from django.db import models

class addrestaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    restaurant = models.ForeignKey(addrestaurant, on_delete=models.CASCADE, related_name='reservations')
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    reservation_date = models.DateTimeField()
    number_of_people = models.PositiveIntegerField(default=1)  # Add default value for existing rows

    def __str__(self):
        return f'Reservation for {self.customer_name} at {self.restaurant.name} on {self.reservation_date}'
    
    
# models.py
from django.db import models

class addhotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(addhotel, related_name='rooms', on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_number} - {self.hotel.name}"

class Booking(models.Model):
    room = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    user = models.CharField(max_length=255)  # Replace this with a ForeignKey to your User model if you have one
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"Booking by {self.user} for room {self.room.room_number}"
    

class Review(models.Model):
    hotel = models.ForeignKey(addhotel, related_name='reviews', on_delete=models.CASCADE)
    user = models.CharField(max_length=255)  # Replace with ForeignKey if you have a User model
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} for hotel {self.hotel.name}"  
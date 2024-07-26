# # customers/models.py

# from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class Reservation(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
#     start_date = models.DateField()
#     end_date = models.DateField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Reservation by {self.user.username} for Room {self.room.room_number} at Hotel {self.hotel.name}"

# class Review(models.Model):
#     restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE, related_name='reviews')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
#     rating = models.PositiveIntegerField()
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Review by {self.user.username} for {self.restaurant.name}"


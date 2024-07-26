from rest_framework import serializers
from .models import addrestaurant, Reservation

class AddRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = addrestaurant
        fields = ['id', 'name', 'description', 'location', 'price']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'restaurant', 'customer_name', 'customer_email', 'reservation_date', 'number_of_people']


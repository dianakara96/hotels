from rest_framework import serializers
from .models import addhotel, Room, Booking, Review

class AddHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = addhotel
        fields = ['id', 'name', 'description', 'location', 'price']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'hotel', 'room_number', 'room_type', 'price', 'available']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'room', 'user', 'check_in', 'check_out']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
# hotel/views.py

# from rest_framework import generics
# from rest_framework.permissions import AllowAny, IsAuthenticated  # Import the needed permission classes
# from .models import addhotel
# from .serializers import AddHotelSerializer

# class AddHotelListCreateView(generics.ListCreateAPIView):
#     queryset = addhotel.objects.all()
#     serializer_class = AddHotelSerializer
#     permission_classes = [AllowAny]  # Allow any user to access this endpoint

# class AddHotelDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = addhotel.objects.all()
#     serializer_class = AddHotelSerializer
#     permission_classes = [IsAuthenticated]  # Example: require authentication for detail, update, and delete

# from django.shortcuts import render, redirect

# from django.shortcuts import render, redirect

# def home(request):
#     return render(request, 'home.html')

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import addhotel, Room, Booking, Review
from .serializers import AddHotelSerializer, RoomSerializer, BookingSerializer, ReviewSerializer


class AddHotelListCreateView(generics.ListCreateAPIView):
    queryset = addhotel.objects.all()
    serializer_class = AddHotelSerializer
    permission_classes = [AllowAny]

class AddHotelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = addhotel.objects.all()
    serializer_class = AddHotelSerializer
    permission_classes = [AllowAny]

class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]  # Restrict access to authenticated users

class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        hotel_id = self.request.query_params.get('hotel')
        if hotel_id:
            return Review.objects.filter(hotel_id=hotel_id)
        return Review.objects.none()  
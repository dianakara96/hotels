# from django.shortcuts import render, redirect


# def home(request):
#     return render(request, 'home.html')

# from rest_framework import generics
# from rest_framework.permissions import AllowAny, IsAuthenticated  # Import the needed permission classes
# from .models import addrestaurant 
# from .serializers import AddRestaurantSerializer

# class AddRestaurantListCreateView(generics.ListCreateAPIView):
#     queryset = addrestaurant.objects.all()
#     serializer_class = AddRestaurantSerializer
#     permission_classes = [AllowAny]  # Allow any user to access this endpoint

# class AddRestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = addrestaurant.objects.all()
#     serializer_class = AddRestaurantSerializer
#     permission_classes = [IsAuthenticated]  # Example: require authentication for detail, update, and delete

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import addrestaurant, Reservation
from .serializers import AddRestaurantSerializer, ReservationSerializer

class AddRestaurantListCreateView(generics.ListCreateAPIView):
    queryset = addrestaurant.objects.all()
    serializer_class = AddRestaurantSerializer
    permission_classes = [AllowAny]  # Allow any user to access this endpoint

class AddRestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = addrestaurant.objects.all()
    serializer_class = AddRestaurantSerializer
    permission_classes = [IsAuthenticated]  # Example: require authentication for detail, update, and delete

class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [AllowAny]  # Allow any user to access this endpoint

class ReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]  # Example: require authentication for detail, update, and delete

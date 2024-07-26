from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')

# dashboard/views.py

# from rest_framework import generics
# from addhotel.models import addhotel  # Import Hotel from hotels app
# from myapp.models import CustomUser  # Import CustomUser from myapp
# from dashboard.serializers import AddHotelSerializer, CustomUserSerializer

# class AddHotelListCreateView(generics.ListAPIView):
#     queryset = addhotel.objects.all()
#     serializer_class = AddHotelSerializer

# class UserListView(generics.ListAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

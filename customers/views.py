# # from django.shortcuts import render, redirect


# # def home(request):
# #     return render(request, 'home.html')

# # customers/views.py

# from rest_framework import viewsets
# from .models import Review, Reservation
# from .serializers import ReviewSerializer, ReservationSerializer

# class ReviewViewSet(viewsets.ModelViewSet):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

# class ReservationViewSet(viewsets.ModelViewSet):
#     queryset = Reservation.objects.all()
#     serializer_class = ReservationSerializer

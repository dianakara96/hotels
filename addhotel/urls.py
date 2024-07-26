# from django.urls import path
# from .views import *
# from . import views



# urlpatterns = [
#     path('', home, name='home'),
   


# ]

# hotel/urls.py

# from django.urls import path
# from .views import AddHotelListCreateView, AddHotelDetailView

# urlpatterns = [
#     path('hotels/', AddHotelListCreateView.as_view(), name='hotel-list-create'),
#     path('hotels/<int:pk>/', AddHotelDetailView.as_view(), name='hotel-detail'),
# ]

from django.urls import path
from .views import AddHotelListCreateView, AddHotelDetailView, RoomListCreateView, RoomDetailView, BookingListCreateView, BookingDetailView, ReviewList

urlpatterns = [
    path('hotels/', AddHotelListCreateView.as_view(), name='hotel-list-create'),
    path('hotels/<int:pk>/', AddHotelDetailView.as_view(), name='hotel-detail'),
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room-detail'),
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('reviews/', ReviewList.as_view(), name='review-list'),

]



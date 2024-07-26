# from django.urls import path
# from .views import *
# from . import views



# urlpatterns = [
#     path('', home, name='home'),
   


# ]

# from django.urls import path
# from .views import AddRestaurantListCreateView, AddRestaurantDetailView

# urlpatterns = [
#     path('restaurant/', AddRestaurantListCreateView.as_view(), name='hotel-list-create'),
#     path('restaurant/<int:pk>/', AddRestaurantDetailView.as_view(), name='hotel-detail'),
# ]

from django.urls import path
from .views import AddRestaurantListCreateView, AddRestaurantDetailView, ReservationListCreateView, ReservationDetailView

urlpatterns = [
    path('restaurant/', AddRestaurantListCreateView.as_view(), name='restaurant-list-create'),
    path('restaurant/<int:pk>/', AddRestaurantDetailView.as_view(), name='restaurant-detail'),
    path('reservations/', ReservationListCreateView.as_view(), name='reservation-list-create'),
    path('reservations/<int:pk>/', ReservationDetailView.as_view(), name='reservation-detail'),
]

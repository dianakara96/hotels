from django.urls import path
from .views import *
from . import views



urlpatterns = [
    path('', home, name='home'),
   


]

# dashboard/urls.py

# from django.urls import path
# from .views import HotelListView, UserListView

# urlpatterns = [
#     path('api/hotels/', HotelListView.as_view(), name='hotel-list'),
#     path('api/users/', UserListView.as_view(), name='user-list'),
# ]

# from django.urls import path
# from .views import *
# from . import views



# urlpatterns = [
#     path('', home, name='home'),
   


# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, MenuViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menus', MenuViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

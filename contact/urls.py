# from django.urls import path
# from .views import *
# from . import views



# urlpatterns = [
#     path('', home, name='home'),
   


# ]

from django.urls import path
from .views import ContactView

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
]

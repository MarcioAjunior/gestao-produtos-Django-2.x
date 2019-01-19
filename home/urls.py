from django.urls import path, include
from .views import index
from .views import my_logout 

urlpatterns = [
    path('', index, name="index"),
    path('logout/', my_logout, name="logout"),
]

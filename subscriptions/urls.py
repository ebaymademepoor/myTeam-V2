from django.urls import path
from .views import checkout

urlpatterns = [
    path('<str:type>', checkout, name="checkout"),
    ]
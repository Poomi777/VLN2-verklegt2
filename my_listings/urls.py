from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/my_listings
    path('', views.index, name="my_listings-index"),
]

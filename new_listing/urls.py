from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/new_listing
    path('', views.index, name="new_listing-index"),
]
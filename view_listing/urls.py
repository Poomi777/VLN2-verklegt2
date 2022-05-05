from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/view_listing
    path('', views.index, name="view_listing-index"),
]

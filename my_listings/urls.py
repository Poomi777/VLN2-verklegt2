from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/my_listings
    path('', views.index, name="my_listings-index"),
    path('<int:id>', views.get_listing_by_id, name="listing-details")
]

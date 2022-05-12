from django.urls import path
from django.contrib.auth.models import User
from . import views

urlpatterns = [
    # http://localhost:8000/my_listings
    path('', views.index, name="my_listings-index"),
    path('<int:id>', views.get_listing_by_id, name="listing_details"),
    path('create_listing', views.create_listing, name="create_listing"),
    path('my_delete_listing/<int:id>', views.my_delete_listing, name="my_delete_listing"),
    path('update_listing/<int:id>', views.update_listing, name="update_listing"),
    path('<int:id>', views.sold_listing, name="Sold_listing"),


]

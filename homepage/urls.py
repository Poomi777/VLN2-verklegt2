from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/homepage
    path('', views.index, name="homepage-index"),
    path('<int:id>', views.get_listing_by_id, name="listing_details"),
    path('delete_listing/<int:id>', views.delete_listing, name="delete_listing"),
    path('update_listing/<int:id>', views.update_listing, name="update_listing"),
]

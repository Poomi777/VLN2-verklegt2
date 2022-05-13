from django.urls import path

import checkout
from checkout.views import index
from . import views

urlpatterns = [
    # http://localhost:8000/my_bids
    path('', views.index, name="my_bids-index"),
    path(r'^<int:id>$', checkout.views.index, name="checkout-index")
    ]
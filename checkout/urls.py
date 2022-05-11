from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/checkout
    path('', views.index, name="checkout-index"),
    path('payment', views.payment, name="payment-index"),
    path('review_order', views.review_order, name="review_order-index"),
    path('order_confirmed', views.order_confirmed, name="order_confirmed-index"),
]
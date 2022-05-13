from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/checkout
    path('<int:id>', views.index, name="checkout-index"),
    path('payment/<int:id>', views.payment, name="payment-index"),
    path('review_order/<int:id>', views.review_order, name="review_order-index"),
    path('order_confirmed/<int:id>', views.order_confirmed, name="order_confirmed-index"),
]
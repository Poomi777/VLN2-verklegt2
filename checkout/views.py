from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'checkout/checkoutindex.html')

def payment(request):
    return render(request, 'checkout/payment.html')

def review_order(request):
    return render(request, 'checkout/review_order.html')

def order_confirmed(request):
    return render(request, 'checkout/order_confirmed.html')
from django.shortcuts import render, get_object_or_404, redirect
from checkout.forms.checkout_form import ShippingCreateForm
from checkout.forms.payment_form import PaymentCreateForm
from checkout.models import Cart

# Create your views here.
def index(request): #Technically def create_shipping_information
    if request.method == 'POST':
        form = ShippingCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment-index')
    else:
        form = ShippingCreateForm()
    return render(request, 'checkout/checkoutindex.html', {
        'form': form})

def payment(request):

    if request.method == 'POST':
        form = PaymentCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_order-index')
    else:
        form = PaymentCreateForm()
    return render(request, 'checkout/payment.html', {
        'form': form})

def review_order(request):
    return render(request, 'checkout/review_order.html')

def order_confirmed(request):
    return render(request, 'checkout/order_confirmed.html')

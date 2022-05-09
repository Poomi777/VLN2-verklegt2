from django.shortcuts import render
from django.http import HttpResponse
from my_listings.models import Listing

# Create your views here.
#mylist = [
#    {'Name': 'mikeay', 'price': 4.99},
#    {'Name': 'dadi', 'price': 50.99},

#]


def index(request):
    context = {'listings': Listing.objects.all().order_by('listing_date')}
    return render(request, 'my_listings/ml_index.html', context)

from django.shortcuts import render, get_object_or_404
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

def get_listing_by_id(request, id):
    return render(request, 'my_listings/listing_details.html', {
        'listing': get_object_or_404(Listing, pk=id)
    })
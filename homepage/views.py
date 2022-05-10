from django.shortcuts import render, get_object_or_404
from my_listings.models import Listing
# Create your views here.
from templates import homepage


def index(request):
    context = {'Listings': Listing.objects.all().order_by('name')}
    return render(request, 'homepage/index.html', context)

def get_listing_by_id(request, id):
    return render(request, 'homepage/listing_details.html', {
        'listing': get_object_or_404(Listing, pk=id)
    })

"""def all_listings_price(request):
    context = {'Listings': Listing.objects.all().order_by('name')}
    return render(request'')"""

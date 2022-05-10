from django.shortcuts import render
from my_listings.models import Listing
# Create your views here.
from templates import homepage


def index(request):
    context = {'Listings': Listing.objects.all().order_by('name')}
    return render(request, 'homepage/index.html', context)

"""def all_listings_price(request):
    context = {'Listings': Listing.objects.all().order_by('name')}
    return render(request'')"""

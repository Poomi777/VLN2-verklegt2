from django.shortcuts import render, get_object_or_404, redirect
from my_listings.models import Listing
from my_listings.forms.listing_form import ListingUpdateForm
from django.http import JsonResponse
# Create your views here.
from templates import homepage


def index(request):
    """if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']

        return JsonResponse({'data': listings})"""
    context = {'Listings': Listing.objects.all().exclude(listing_highest_offer='-10').order_by('name')}
    return render(request, 'homepage/index.html', context)


def get_listing_by_id(request, id):
    return render(request, 'homepage/listing_details.html', {
        'listing': get_object_or_404(Listing, pk=id),
        'searchuser': request.user.id,
    })
def delete_listing(request, id):
    listing = get_object_or_404(Listing, pk=id)
    listing.delete()
    return redirect('homepage-index')

def update_listing(request, id):
    instance = get_object_or_404(Listing, pk=id)
    if request.method == 'POST':
        form = ListingUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('listing_details', id=id)
    else:
        form = ListingUpdateForm(instance=instance)
    return render(request, 'my_listings/update_listing.html', {
        'form': form,
        'id': id
    })


"""def all_listings_price(request):
    context = {'Listings': Listing.objects.all().order_by('name')}
    return render(request'')"""

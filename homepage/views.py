from django.shortcuts import render, get_object_or_404, redirect

from my_bids.forms.MakeBidForm import BidsCreateForm
from my_listings.models import Listing
from my_listings.forms.listing_form import ListingUpdateForm
from my_bids.models import Bids
from my_bids.forms import MakeBidForm
from django.http import JsonResponse
# Create your views here.
from templates import homepage
from userprofile.models import Userinfo


def index(request):
    if request.GET.get('search'):
        listing = Listing.objects.all().exclude(listing_highest_offer='-10').order_by('name').filter(name__icontains=request.GET.get('search'))
    else:
        listing = Listing.objects.all().exclude(listing_highest_offer='-10').order_by('name')

    userinfovar = Userinfo.objects.filter(userinfo_id=request.user).first()
    context = {'Listings': listing,
               'userprofile': get_object_or_404(Userinfo, userinfo_id=userinfovar.userinfo_id)}
    return render(request, 'homepage/index.html', context)


def get_listing_by_id(request, id):
    userinfovar = Userinfo.objects.filter(userinfo_id=request.user).first()
    form = BidsCreateForm(request.POST or None)
    if form.is_valid():
        # if form value is greater than bid highest
        # add to my bids
        # update listing bid highest

        # form value = form.value
        # if yes =
        curr_listing = Listing.objects.get(pk=id)

        if form.data['bid_price'] > curr_listing.listing_highest_offer:
            curr_listing.listing_highest_offer = form.data['bid_price']
            curr_listing.save()
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.product_id = Listing.objects.get(listing_id=id)
            instance.save()


        else:
            print("the offer is not high enough")

        return redirect('/')

    return render(request, 'homepage/listing_details.html', {
        'listing': get_object_or_404(Listing, pk=id),
        'searchuser': request.user.id,
        'form': form,
        'userprofile': get_object_or_404(Userinfo, userinfo_id=userinfovar.userinfo_id)
    })


def delete_listing(request, id):
    listing = get_object_or_404(Listing, pk=id)
    listing.delete()
    return redirect('homepage-index')

def update_listing(request, id):
    userinfovar = Userinfo.objects.filter(userinfo_id=request.user).first()
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
        'id': id,
        'userprofile': get_object_or_404(Userinfo, userinfo_id=userinfovar.userinfo_id)
    })

def make_bid(request, id):
    userinfovar = Userinfo.objects.filter(userinfo_id=request.user).first()
    bids = get_object_or_404(Bids)
    if request.method == 'POST':
        form = BidsCreateForm(data=request.POST, bids=bids)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user.id
            instance.product_id = id
            instance.save()
            return redirect('/')
    else:
        form = BidsCreateForm()
    return render(request, 'homepage/listing_details.html', {
        'form': form,
        'userprofile': get_object_or_404(Userinfo, userinfo_id=userinfovar.userinfo_id)
    })


"""def all_listings_price(request):
    context = {'Listings': Listing.objects.all().order_by('name')}
    return render(request'')"""

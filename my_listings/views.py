from django.shortcuts import render, get_object_or_404, redirect

from my_bids.models import Bids
from my_listings.forms.listing_form import ListingCreateForm, ListingUpdateForm, Listing_Selling_Update
from my_listings.models import Listing
from userprofile.models import User, Userinfo
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

# Create your views here.
# mylist = [
#    {'Name': 'mikeay', 'price': 4.99},
#    {'Name': 'dadi', 'price': 50.99},

# ]


"""def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        listings = [ {
            'listing_id': x.listing_id,
            'name': x.name,
            'listing_price': x.listing_price,
            'listing_image_url': x.listing_image_url
        } for x in Listing.objects.filter(name__icontains=search_filter) ]
        return JsonResponse({'data': listings})
    context = {'listings': Listing.objects.all().order_by('listing_date')}
    return render(request, 'my_listings/ml_index.html', context)"""


def index(request):
    userinfovar = Userinfo.objects.filter(userinfo_id=request.user).first()
    current_user = request.user

    form = None

    if request.method == 'POST':
        listing_id = request.POST.get('listingid')
        listingoffer = request.POST.get('listingoffer')
        listing = Listing.objects.get(pk=listing_id)
        print(listingoffer, listing_id)
        wonbid = Bids.objects.get(listing_id=listing_id, bid_price=listingoffer)
        wonbid.bid_accepted = True
        listing.listing_sold = True
        listing.save()
        wonbid.save()

    else:
        form = Listing_Selling_Update(request.POST or None)

    context = {
        'form': form,
        'listings': Listing.objects.filter(user_id_id=current_user.id).order_by('listing_date'),
        'userprofile': get_object_or_404(Userinfo, userinfo_id=userinfovar.userinfo_id)
    }
    return render(request, 'my_listings/ml_index.html', context)


def get_listing_by_id(request, id):
    instance = Userinfo.objects.filter(userinfo_id=request.user).first()
    return render(request, 'my_listings/listing_details.html', {
        'listing': get_object_or_404(Listing, pk=id),
        'searchuser': request.user.id,
        'userprofile': get_object_or_404(Userinfo, userinfo_id=instance.userinfo_id)
    })


def create_listing(request):
    userinfovar = Userinfo.objects.filter(userinfo_id=request.user).first()
    if request.method == 'POST':
        form = ListingCreateForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
            return redirect('my_listings-index')
    else:
        form = ListingCreateForm()
    return render(request, 'my_listings/create_listing.html', {
        'form': form,
        'userprofile': get_object_or_404(Userinfo, userinfo_id=userinfovar.userinfo_id)
    })


def my_delete_listing(request, id):
    listing = get_object_or_404(Listing, pk=id)
    listing.delete()
    return redirect('homepage-index')


def update_listing(request, id):
    instance = get_object_or_404(Listing, pk=id)
    userinfovar = Userinfo.objects.filter(userinfo_id=request.user).first()
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


def sold_listing(request, id):
    instance = get_object_or_404(Listing, pk=id)
    userinfovar = Userinfo.objects.filter(userinfo_id=request.user).first()
    if request.method == 'POST':
        form = Listing_Selling_Update(data=request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.listing_highest_offer = '-10'
            instance.save()
            return redirect('/')
    else:
        form = Listing_Selling_Update(instance=instance)
    return render(request, 'my_listings/ml_index.html', {
        'form': form,
        'id': id,
        'userprofile': get_object_or_404(Userinfo, userinfo_id=userinfovar.userinfo_id)
    })


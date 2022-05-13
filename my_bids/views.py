from django.shortcuts import render, get_object_or_404

from my_bids.models import Bids
from userprofile.models import Userinfo
from my_listings.models import Listing

# Create your views here.



def index(request):
    userinfovar = Userinfo.objects.filter(userinfo_id=request.user).first()
    user = request.user
    ids = list()
    for i in Bids.objects.all():
        if i.buyer_id == user:
            ids.append(i.listing_id_id)
    mybids = Bids.objects.filter(buyer_id=user)
    listings = Listing.objects.filter(listing_id__in=ids)
    return render(request, 'my_bids/mbindex.html', {
        'userprofile': get_object_or_404(Userinfo, userinfo_id=userinfovar.userinfo_id),
        'listings': listings,
        'mybids': mybids
    })


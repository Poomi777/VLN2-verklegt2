from django.shortcuts import render, get_object_or_404


# Create your views here.
from userprofile.models import Userinfo


def index(request):
    userinfovar = Userinfo.objects.filter(userinfo_id=request.user).first()
    return render(request, 'my_bids/mbindex.html', {
        'userprofile': get_object_or_404(Userinfo, userinfo_id=userinfovar.userinfo_id)
    })
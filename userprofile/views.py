from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from userprofile.forms.Userinfo import UserinfoForm
from userprofile.models import Userinfo
# Create your views here.


"""my_profile = [
    {'Name': 'danni', 'Image': 'static/images/'},
]"""
#def index(request):
    #return render(request, 'userprofile/profile_index.html')


def userinforegister(request):
    instance = Userinfo.objects.filter(userinfo_id=request.user).first()
    if request.method == 'POST':
        form = UserinfoForm(instance=instance, data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.userinfo_id = request.user
            instance.save()
            return redirect('profile')

    if instance == None:
        return render(request, 'userprofile/profile_index.html', {
            'form': UserinfoForm(instance=instance)})

    return render(request, 'userprofile/profile_index.html', {
        'form': UserinfoForm(instance=instance),
        'userprofile': get_object_or_404(Userinfo, userinfo_id=instance.userinfo_id)
    })


    """if request.method == 'POST':
        form = UserinfoForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.userID = request.user
            instance.save()
            return redirect('homepage-index')

    return render(request, 'userprofile/register.html', {
        'form': UserinfoForm()
    })"""


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
           # userinforegister(request)
            return redirect('login')

    return render(request, 'userprofile/login.html', {
        'form': UserCreationForm()
    })
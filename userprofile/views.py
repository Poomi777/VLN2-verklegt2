from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from userprofile.forms.Userinfo import UserinfoForm
# Create your views here.


"""my_profile = [
    {'Name': 'danni', 'Image': 'static/images/'},
]"""
def index(request):
    return render(request, 'userprofile/profile_index.html')


def userinforegister(request):
    if request.method == 'POST':
        form = UserinfoForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.userID = request.user
            instance.save()
            return redirect('homepage-index')

    return render(request, 'userprofile/register.html', {
        'form': UserinfoForm()
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            userinforegister(request)
            return redirect('login')

    return render(request, 'userprofile/register.html', {
        'form': UserCreationForm()
    })
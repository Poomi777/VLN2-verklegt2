from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from userprofile.forms.Userinfo import UserinfoForm
# Create your views here.


"""my_profile = [
    {'Name': 'danni', 'Image': 'static/images/'},
]"""
def index(request):
    return render(request, 'userprofile/profile_index.html')

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

def userinforegister(request):
    if request.method == 'POST':
        form = UserinfoForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.name = request.user.username
            return redirect('my_listings-index')
        else:
            form = UserinfoForm()
    return render(request, 'userprofile/register.html', {
        'form': form
    })

"""def myprofile(request):
    return render(request, 'navigation.html', context={'my_profile': myprofile})"""


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

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
            return redirect('login')
    return render(request, 'userprofile/register.html', {
        'form': UserCreationForm()
    })

"""def myprofile(request):
    return render(request, 'navigation.html', context={'my_profile': myprofile})"""


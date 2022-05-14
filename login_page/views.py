from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from userprofile.forms.Userinfo import UserinfoForm
from userprofile.models import Userinfo
# Create your views here.

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            # userinforegister(request)
            return redirect('login')

    return render(request, 'homepage/index.html', {
        'form': UserCreationForm()
    })
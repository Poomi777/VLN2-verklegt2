from django.shortcuts import render

# Create your views here.
my_profile = [
    {'Name': 'danni', 'Image': 'static/images/'},
]
def index(request):
    return render(request, 'userprofile/profile_index.html')

def myprofile(request):
    return render(request, 'navigation.html', context={'my_profile': myprofile})


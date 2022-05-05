from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
mylist = [
    {'Name': 'mikeay', 'price': 4.99},
    {'Name': 'dadi', 'price': 50.99},

]


def index(request):
    return render(request, 'my_listings/ml_index.html', context={'mylist': mylist})

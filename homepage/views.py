from django.shortcuts import render

# Create your views here.
from templates import homepage


def index(request):
    return render(request, 'homepage/index.html')



from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from templates import homepage


def index(request):
    return render(request, 'homepage/homepage.html'),



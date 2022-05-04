from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import homepage


def index(request):
    return render("/templates/homepage/homepage.html"),



from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from templates import homepage


def index(request):
    context = {}
    return render(request, 'homepage/index.html', context),



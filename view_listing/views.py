from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'view_listing/vl_index.html')

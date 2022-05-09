from django.shortcuts import render
from categories.models import ListingCategory





def index(request):
    context = {'My_categorires': ListingCategory.objects.all().order_by('name')}
    return render(request, 'categories/categoriesindex.html', context)


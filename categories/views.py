from django.shortcuts import render

My_categorires = [
    {'Categorie': 'Tech', 'Product': 'Iphone'},
    {'Categorie': 'Housing', 'product': 'Bread'},

]

def index(request):
    return render(request, 'categories/categoriesindex.html', context={'My_categorires': My_categorires})


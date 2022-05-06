from django.shortcuts import render

My_categorires = [
    {'Categorie': 'Tech', 'Product': 'Iphone','price': 699.99},
    {'Categorie': 'Housing', 'product': 'Bread', 'Price': 6.99},

]

def index(request):
    context = {'My_categorires': My_categorires}
    return render(request, 'categories/categoriesindex.html', context)


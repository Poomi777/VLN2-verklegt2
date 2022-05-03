from django.shortcuts import render

candies = [
    { 'name': 'smarties', 'price': 5.99 },
    { 'name': 'skittles', 'price': 4.99 },
]

# Create your views here.
def index(request):
    return render(request, 'candy/index.html', context={ 'candies': candies })
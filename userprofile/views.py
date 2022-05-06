from django.shortcuts import render

# Create your views here.
My_profile = [
    {'Name': 'ddaa', 'Image':'static/images/'},
    {'Name': 'Daniel', 'Image': 'static/images/'}

]
def index(request):
    context = {'My_profile': My_profile}
    return render(request, 'userprofile/profile_index.html',context)


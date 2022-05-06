from django.shortcuts import render

# Create your views here.
My_profile = [
    {'Name': 'Daniel', 'Image':'testprofile'}

]
def index(request):
    profile = {'My_profile': My_profile}
    return render(request, 'userprofile/profile_index.html',context='profile')


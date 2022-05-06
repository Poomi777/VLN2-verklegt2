from django.shortcuts import render

# Create your views here.
My_profile = [
    {'Name': 'ddaa', 'Image':'insertpicture '},
    {'Name': 'Daniel', 'Image':'insertpicture'}

]
def index(request):
    context = {'My_profile': My_profile}
    return render(request, 'userprofile/profile_index.html',context)


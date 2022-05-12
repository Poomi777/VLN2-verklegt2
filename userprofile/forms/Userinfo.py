from django.forms import ModelForm, widgets
from userprofile.models import Userinfo

class UserinfoForm(ModelForm):


    class Meta:
        model = Userinfo
        exclude = ['address', 'country', 'rating', 'image']


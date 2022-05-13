from django.forms import ModelForm, widgets
from userprofile.models import Userinfo

class UserinfoForm(ModelForm):


    class Meta:
        model = Userinfo
        exclude = ['userinfo_id']
        widgets = {
            'address': widgets.TextInput(attrs={ 'class': 'form-control'}),
            'country': widgets.TextInput(attrs={ 'class': 'form-control'}),
            'rating': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'image': widgets.TextInput(attrs={ 'class': 'form-control'})
}
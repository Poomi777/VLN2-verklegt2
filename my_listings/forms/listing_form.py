from django.forms import ModelForm, widgets
from django import forms
from my_listings.models import Listing


class ListingCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Listing
        exclude = ['listing_id', 'listing_highest_offer', 'user_id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'listing_description': widgets.TextInput(attrs={'class': 'form-control'}),
            'listing_category': widgets.Select(attrs={'class': 'form-control'}),  # kíkja á þetta aftur
            'listing_price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'listing_condition': widgets.NumberInput(attrs={'class': 'form-control'}),
            # 'listing_date': widgets.???????
            # 'on-sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }

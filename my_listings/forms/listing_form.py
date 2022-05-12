from django.forms import ModelForm, widgets
from django import forms
from my_listings.models import Listing
from django.contrib.auth.models import auth, User

CONDITION_CHOICES = [('5', 'Perfect'),
                     ('4', 'Great'),
                     ('3', 'Good'),
                     ('2', 'Bad'),
                     ('1', 'Horrible'),
                     ]


class ListingCreateForm(ModelForm):
    #listing_image_url = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # condition = forms.MultipleChoiceField(
                   # required=True,
                   # widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
                   # choices=CONDITION_CHOICES,)

    class Meta:
        model = Listing
        exclude = ['listing_id', 'listing_highest_offer', 'user_id', 'listing_date']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'listing_description': widgets.TextInput(attrs={'class': 'form-control'}),
            'listing_category': widgets.Select(attrs={'class': 'form-control'}),  # kíkja á þetta aftur
            'listing_price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'listing_condition': widgets.RadioSelect(attrs={'class': 'checkbox'}, choices=CONDITION_CHOICES),
            'listing_image_url': widgets.TextInput(attrs={'class': 'form_control', 'required': True})

            # 'on-sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }


class ListingUpdateForm(ModelForm):

    class Meta:
        model = Listing
        exclude = ['listing_id', 'listing_highest_offer', 'user_id', 'listing_date']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'listing_description': widgets.TextInput(attrs={'class': 'form-control'}),
            'listing_category': widgets.Select(attrs={'class': 'form-control'}),  # kíkja á þetta aftur
            'listing_price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'listing_condition': widgets.RadioSelect(attrs={'class': 'checkbox'}, choices=CONDITION_CHOICES),
            'listing_image_url': widgets.TextInput(attrs={'class': 'form_control', 'required': True})
            # 'on-sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }

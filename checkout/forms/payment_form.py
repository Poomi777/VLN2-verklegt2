from django.forms import ModelForm, widgets
from django import forms
from checkout.models import Payment

class PaymentCreateForm(ModelForm):

    class Meta:
        model = Payment
        exclude = ['cart_id', 'user_id']
        widgets = {
            'cardholder_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'month_expiration': widgets.NumberInput(attrs={'class': 'form-control'}),
            'year_expiration': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control'}) # Figure out how to limit size to 3

            # 'name': widgets.TextInput(attrs={'class': 'form-control'}),
            # 'listing_description': widgets.TextInput(attrs={'class': 'form-control'}),
            # 'listing_category': widgets.Select(attrs={'class': 'form-control'}),  # kíkja á þetta aftur
            # 'listing_price': widgets.NumberInput(attrs={'class': 'form-control'}),
            # 'listing_condition': widgets.RadioSelect(attrs={'class': 'checkbox'}, choices=CONDITION_CHOICES),
            # 'listing_image_url': widgets.TextInput(attrs={'class': 'form_control', 'required': True})
            # 'on-sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }

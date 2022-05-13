from django.forms import ModelForm, widgets
from my_bids.models import Bids
from my_listings.models import Listing

class BidsCreateForm(ModelForm):

    class Meta:
        model = Bids
        exclude = ['user_id', 'product_id', 'bid_accepted']
        widgets = {
            'bid_price': widgets.NumberInput(attrs={'class': 'form-control'})
        }
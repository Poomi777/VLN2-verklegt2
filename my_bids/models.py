from django.db import models
from my_listings.models import Listing
from userprofile.models import User

# Create your models here.


class Bids(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey(Listing, on_delete=models.SET_NULL, null=True)
    bid_price = models.FloatField()
    bid_accepted = models.BooleanField(null=True)

    def __str__(self):
        return self.bid_price
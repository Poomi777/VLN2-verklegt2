from django.db import models
from my_listings.models import Listing
from userprofile.models import User

# Create your models here.


class Bids(models.Model):
    user_id = models.ForeignKey(User)
    product_id = models.ForeignKey(Listing)
    bid_price = models.FloatField()
    bid_accepted = models.NullBooleanField()

    def __str__(self):
        return self.bid_price
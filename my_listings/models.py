from django.db import models

from categories.models import ListingCategory

from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.


class Listing(models.Model):
    listing_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    listing_category = models.ForeignKey(ListingCategory, on_delete=models.SET_NULL, null=True)
    listing_description = models.CharField(max_length=500)
    listing_condition = models.IntegerField()
    listing_price = models.FloatField()
    listing_highest_offer = models.CharField(max_length=30, default=0)
    listing_image_url = models.CharField(max_length=500)
    listing_date = models.DateField(default=timezone.now)
    listing_sold = models.BooleanField(default=False)

    def __str__(self):
       return self.name

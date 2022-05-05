from django.db import models
from categories.models import ListingCategory
from userprofile.models import User


# Create your models here.


class Listing(models.Model):
    listing_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30)
    listing_category = models.ForeignKey(LinkCategory, on_delete=models.SET_NULL, null=True)
    listing_description = models.CharField(max_length=500)
    listing_condition = models.IntegerField()
    listing_price = models.FloatField()
    listing_highest_offer = models.ForeignKey(Offers, on_delete=models.SET_NULL, null=True)
    listing_image_url = models.CharField(max_length=500, default="https://d25tv1xepz39hi.cloudfront.net/2016-07-16/files/cat-sample_1313.jpg")

    def __str__(self):
        return self.link

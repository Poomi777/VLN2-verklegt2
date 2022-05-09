from django.db import models
from userprofile.models import User

# Create your models here.


class Cart(models.Model):
    cart_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    street_name = models.CharField(max_length=30, null=False, blank=False)
    apartment_number = models.CharField(max_length=30, null=False, blank=False)
    city = models.CharField(max_length=30, null=False, blank=False)
    country = models.CharField(max_length=30, null=False, blank=False)
    postal_code = models.IntegerField()

    def __str__(self):
        pass
        #return self.name


class Payment(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cardholder_name = models.CharField(max_length=30, null=False, blank=False)
    card_number = models.IntegerField()
    month_expiration = models.IntegerField()
    year_expiration = models.IntegerField()
    cvc = models.IntegerField()


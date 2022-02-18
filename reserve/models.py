from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from Bikes.models import UploadDetails


class Book(models.Model):
    bike = models.ForeignKey(UploadDetails, on_delete=models.SET_NULL, null=True, related_name="rooms")
    number = models.IntegerField(default=1)

    def bike_price(self):
        return self.number * self.bike.bike_price


class Reserve(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bikes = models.ManyToManyField(Book)

    def get_bikes(self):
        return self.bikes.all()

    def get_total(self):
        total = 0
        for order_item in self.bikes.all():
            total += order_item.bike_price()
        return total

from django.db import models


# Create your models here.
class UserDetails(models.Model):
    First_Name = models.CharField(max_length=40)
    Last_Name = models.CharField(max_length=40)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)

    def __str__(self):
        return self.Email


class UploadDetails(models.Model):
    Bikename = models.CharField(max_length=200)
    EngineDisplacement = models.IntegerField()
    maxpower = models.IntegerField()
    maxtorque = models.IntegerField()
    Fuel = models.CharField(max_length=500)
    Company = models.CharField(max_length=500, default='')
    Gear = models.IntegerField()
    Price = models.IntegerField()
    Desc = models.CharField(max_length=500)
    file = models.FileField(upload_to='media', default='')

    def __str__(self):
        return self.Desc

    def uploadata_fields_blank(self):
        return(self.Desc!= False)

    def TestBike_Price(self):
        return ((self.Price) >= 3500.00)

    def TestCompanyAndBikeDesc(self):
        return (self.Company != self.Desc)
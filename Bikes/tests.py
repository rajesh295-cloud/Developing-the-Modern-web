from django.test import TestCase
from Bikes.models import UploadDetails


class ModelTestCase(TestCase):

    def testBike_Price(self):
        a1 = UploadDetails.objects.create(Company="Honda", Bikename="hero", Price=50000,
                                          Desc="Nice Bike", Gear=5,
                                          EngineDisplacement=300, maxtorque=88, maxpower=60, fuel="fi")
        value = a1.TestBike_Price
        self.assertEqual(value)

    def test_CompanyAndBikeDesc(self):
        a2 = UploadDetails.objects.create(Company="Honda", Bikename="hero", Price=50000,
                                          Desc="Nice Bike", Gear=5,
                                          EngineDisplacement=300, maxtorque=88, maxpower=60, fuel="fi")
        value2 = a2.TestCompanyAndBikeDesc()
        self.assertTrue(value2)

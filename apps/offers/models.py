from django.db import models

class Passes(models.Model):
    namePass = models.CharField(max_length=150,verbose_name="Name of the Pass")
    daysOfUse = models.IntegerField(default=0,verbose_name="Days of use")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Price")
    active = models.BooleanField(default=True,verbose_name="Active")

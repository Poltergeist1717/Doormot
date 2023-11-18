from django.db import models
#from django.contrib.auth.models import User

class Individual_owner_profile(models.Model):
    #Individual_owner_profile = models.OneToOneField(on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)

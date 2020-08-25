from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserProfileInfo(models.Model):

     # Create relationship (don't inherit from User!) 
     #make sure you have install "pip install pylint-django"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # make sure to inatall: pip install django-phonenumber-field[phonenumberslite]
    phone_number = PhoneNumberField()

    
    def __str__(self):
        return self.user.username

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

     # Create relationship (don't inherit from User!) 
     #make sure you have install "pip install pylint-django"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # pip install pillow to use ImageField!
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+91 9876543210'. Up to 13 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    
    def __str__(self):
        return self.user.username

from django.db import froms
from django.contrib.auth.models import User
from usersAccount.models import UserProfileInfo

class UserForm(froms.ModelForm):
    password = froms.CharFiled(widget=froms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'firstName', 'lastName', 'email', 'phoneNumber')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields=('profile_pic')
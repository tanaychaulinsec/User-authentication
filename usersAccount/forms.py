from django import forms
from django.contrib.auth.models import User
from usersAccount.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))
    
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password' )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your user name'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter your email address'}),    
        }
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('phone_number',)
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your phone number'})
        }
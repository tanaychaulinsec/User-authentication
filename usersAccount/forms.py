from django import forms
from django.contrib.auth.models import User
from usersAccount.models import UserProfileInfo
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password again'}))

    # Validating password
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError("Password don't match")

        return cd['password2']

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password' )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),   
        }
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('phone_number',)
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your phone number'}),
        }
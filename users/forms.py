from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'required': True, 'id': 'firstName'}))
    #first_name = forms.CharField(max_length=30, required=True, widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName', 'required': True, 'id': 'userName'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'required': True, 'id': 'lastName'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget= forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required': True, 'id': 'email'}))
    phoneNo = forms.CharField(max_length=15,widget= forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Phone No', 'required': True, 'id': 'phoneNo'}))
    roomId = forms.CharField(max_length=10, widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Room Id', 'id': 'roomId', 'required': True}))
    password1 = forms.CharField(required=True, widget= forms.PasswordInput(attrs= {'class': 'form-control', 'id': 'create-password', 'required': True, 'placeholder': 'Create Password'}))
    password2 = forms.CharField(required=True, widget= forms.PasswordInput(attrs= {'class': 'form-control', 'id': 'con-password', 'required': True, 'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ('username', 'last_name', 'phoneNo', 'roomId', 'email', 'password1', 'password2')
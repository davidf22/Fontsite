from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauth.models import UserAccount


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'johndoe@gmail.com'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '*******'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '*******'}))

    class Meta:
        model = UserAccount
        fields = ['email', 'password1', 'password2']


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'johndoe@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '*******'}))

    class Meta:
        model = UserAccount
        fields = ['email', 'password']
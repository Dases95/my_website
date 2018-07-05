from django import forms
from django.contrib.auth.models import User
from Store.models  import UserProfile


class loginForm(forms.Form):
    username = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your e-mail"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your Password"  
            }
        )
    )
class UserForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "username    "
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your e-mail"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your Password"
            }
        )
    )
    class Meta():
        model = User
        fields = ('username','email','password')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model= UserProfile
        fields =('picture',)

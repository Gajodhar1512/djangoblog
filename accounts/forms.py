from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class User_reg_form(UserCreationForm):
    gender_choices = [
        ('M', 'Male'),
        ('F', "Female"),
        ('O', 'Other')
    ]
    email = forms.EmailField()
    profile_pic = forms.ImageField()
    gender = forms.ChoiceField(choices=gender_choices)

    class Meta:
        model = User  # User is an inbuilt class in django
        fields = ['username', 'profile_pic', 'email', 'gender', 'password1', 'password2']

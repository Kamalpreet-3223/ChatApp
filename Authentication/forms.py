from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import fields


class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'email': 'Email'
        }


class updateProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'date_joined', 'last_login']
        labels = {
            'email': 'Email'
        }


class updateAdminProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'email': 'Email'
        }

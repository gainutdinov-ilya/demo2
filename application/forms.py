from django.contrib.auth.forms import UserCreationForm
from django import forms

from application.models import User, Order

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

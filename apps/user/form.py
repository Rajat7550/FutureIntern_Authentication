from django import forms
from apps.user.models import User


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password']
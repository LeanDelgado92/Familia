from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        

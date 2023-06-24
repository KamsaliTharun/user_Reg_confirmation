from app.models import * 
from django import forms


class userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        # widgets = {'password' : forms.PasswordInput,
        # 'username':forms.TextInput(attrs = {'class':'form-control'}),
        # 'email':forms.TextInput(attrs = {'class':'form-control'}),
        # }
        help_texts = {'username' : ""}


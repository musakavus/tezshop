from django import forms
from .models import Registration


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Registration
        fields = [
            'first_name', 'last_name', 'email', 'password', 'password_confirmation',
            'phone', 'company', 'address1', 'address2', 'city', 'postal_code', 'country', 'region',

        ]


class LoginForm(forms.Form):
    email = forms.EmailField(label='E-Posta')
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput)

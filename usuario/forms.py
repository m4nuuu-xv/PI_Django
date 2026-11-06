
from django import forms


class LoginForm(forms.Form):

    matricula = forms.RegexField(
        regex=r'^\d{8,14}$',
        label='Matrícula',
        error_messages={
            'invalid': 'A matrícula deve conter de 8 a 14 números.'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua matrícula',
            'autofocus': True,
        })
    )

    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
        })
    )

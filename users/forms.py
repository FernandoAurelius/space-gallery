from django import forms

class LoginForm(forms.Form):
    login_name = forms.CharField(
        label='Nome de Login', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs=
            {'class':'form-control',
             'placeholder':'Ex.: José Santos'}))
    
    password = forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70, 
        widget=forms.PasswordInput(
            attrs=
            {'class':'form-control',
             'placeholder':'Digite sua senha'}))
    
class RegistForm(forms.Form):
    regist_name = forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs=
            {'class':'form-control',
             'placeholder':'Ex.: José Santos'})
    )

    regist_email = forms.CharField(
        label='Email de Cadastro',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs=
            {'class':'form-control',
             'placeholder':'Ex.: jose@santos.com'})
    )

    regist_password = forms.CharField(
        label='Senha de Cadastro', 
        required=True, 
        max_length=70, 
        widget=forms.PasswordInput(
            attrs=
            {'class':'form-control',
             'placeholder':'Digite sua senha'}))
    
    confirm_password = forms.CharField(
        label='Senha de Confirmação', 
        required=True, 
        max_length=70, 
        widget=forms.PasswordInput(
            attrs=
            {'class':'form-control',
             'placeholder':'Digite sua senha novamente'}))
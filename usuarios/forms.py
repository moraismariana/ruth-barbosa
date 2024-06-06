from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'cadastro-input',
                'placeholder': 'Nome',
            }
        )
    )
    senha_login=forms.CharField(
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'login-input',
                'placeholder': 'Senha',
            }
        )
    )

class CadastroForms(forms.Form):
    nome=forms.CharField(
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'cadastro-input',
                'placeholder': 'Nome',
            }
        )
    )
    
    sobrenome=forms.CharField(
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'cadastro-input',
                'placeholder': 'Sobrenome',
            }
        )
    )

    telefone=forms.CharField(
        required=True,
        max_length=12,
        widget=forms.TextInput(
            attrs={
                'class': 'cadastro-input',
                'placeholder': 'Tefelone',
            }
        )
    )

    email_cadastro=forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'cadastro-input',
                'placeholder': 'Email',
            }
        )  
    )

    senha_cadastro=forms.CharField(
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'cadastro-input',
                'placeholder': 'Senha',
            }
        )
    )
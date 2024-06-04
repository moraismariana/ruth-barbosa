from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User

def login(request):
    form = LoginForms()
    return render(request, 'login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        #ação que irá tomar caso o formulário seja válido (armazenar os valores recebidos em um BD)
        if form.is_valid():
            nome=form['nome'].value()
            sobrenome=form['sobrenome'].value()
            telefone=form['telefone'].value()
            email_cadastro=form['email_cadastro'].value()
            senha_cadastro=form['senha_cadastro'].value()

            #verifica se já existe usuário com esse email
            if User.objects.filter(email=email_cadastro).exists():
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                last_name=sobrenome,
                email=email_cadastro,
                password=senha_cadastro,
            )
            usuario.save()
            return redirect('login')

    return render(request, 'cadastro.html', {'form': form})

def pagina_usuario(request):
    return render(request, 'usuario.html')
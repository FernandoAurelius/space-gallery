from django.shortcuts import render, redirect

from django.contrib import auth, messages
from django.contrib.auth.models import User

from users.forms import LoginForm, RegistForm

def login(request):
    form = LoginForm()

    if request.method == 'POST':

            form = LoginForm(request.POST)

            if form.is_valid():
                name = form['login_name'].value()
                password = form['password'].value()

            user = auth.authenticate(request, username=name, password=password)

            if user is not None:
                auth.login(request, user=user)
                messages.success(request, f'Usuário(a) {name} logado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Erro ao efetuar login: usuário ou senha incorretos!')
                return redirect('login')

    return render(request, 'users/login.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso')
    return redirect('login')

def registration(request):

    form = RegistForm()

    if request.method == 'POST':
        
        form = RegistForm(request.POST)
        
        if form.is_valid():
            if form['regist_password'].value() != form['confirm_password'].value():
                messages.error(request, 'Senhas não são iguais!')
                return redirect('registration')
            
            name = form['regist_name'].value()
            email = form['regist_email'].value()
            password = form['regist_password'].value()

            if User.objects.filter(username=name).exists():
                messages.error(request, 'Nome de usuário já existe!')
                return redirect('registration')
            
            user = User.objects.create_user(username=name, email=email, password=password)
            user.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')

    return render(request, 'users/registration.html', {'form': form})
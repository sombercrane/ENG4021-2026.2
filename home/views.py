
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

@login_required
def home(request):
    return render(request, 'home.html')


def cadastrar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username and email and password:
            if User.objects.filter(username=username).exists():
                return render(request, 'cadastro.html', {
                    'erro': 'Este nome de usuário já existe.'
                })

            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            return redirect('login')

    return render(request, 'cadastro.html')


def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('home')

        return render(request, 'login.html', {
            'erro': 'Usuário ou senha incorretos.'
        })

    return render(request, 'login.html')


def logout_usuario(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    return redirect('home')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Jogo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    jogos_fixos = [
        {'nome': 'Red Dead Redemption', 'imagem': 'reddead1.jpg', 'link': '/jogos/reddead1/'},
        {'nome': 'Red Dead Redemption 2', 'imagem': 'reddead2.jpg', 'link': '/jogos/reddead2/'},
    ]

    termo_busca = request.GET.get('busca', '')
    if termo_busca:
        jogos_dinamicos = Jogo.objects.filter(nome__icontains=termo_busca)
    else:
        jogos_dinamicos = Jogo.objects.all()

    context = {
        'jogos_fixos': jogos_fixos,
        'jogos_dinamicos': jogos_dinamicos,
        'busca': termo_busca,
    }
    return render(request, 'loja/index.html', context)

def jogo_reddead1(request):
    return render(request, 'loja/reddead1.html')

def jogo_reddead2(request):
    return render(request, 'loja/reddead2.html')

def detalhes_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)
    return render(request, 'loja/detalhes_jogo.html', {'jogo': jogo})

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if not User.objects.filter(username=nome).exists():
            User.objects.create_user(username=nome, email=email, password=senha)
            return redirect('login')
        else:
            return render(request, 'cadastro.html', {'erro': 'Nome de usuário já existe.'})
    return render(request, 'cadastro.html')

def login_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        usuario = authenticate(request, username=nome, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            return render(request, 'login.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
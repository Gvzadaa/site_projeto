from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')


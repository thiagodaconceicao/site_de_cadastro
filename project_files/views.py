from django.shortcuts import render
from .models import Usuario
from django.contrib.auth.hashers import make_password
def home(request):
    return render(request,"usuarios/home.html")
def usuario(request):
    #salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()
    #Exibir todos os usuairos cadastrado 
    usuarios = {
        'usuarios': Usuario.objects.all
    }
    #Retorno os dados para a pagina
    return render(request, 'usuarios/usuarios.html', usuarios)

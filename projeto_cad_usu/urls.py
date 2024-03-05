
from django.urls import path
from app_cad_usu import views
urlpatterns = [
    #rota,view responsável, nome referencia
    #usuarios.com
    path('', views.home,name='home'),
    #usuarios.com/usuarios
    path('usuarios/', views.usuario, name="listagem_usuarios")
]

from django.contrib import admin
from django.urls import path
from project_files import views
urlpatterns = [
    #rota,view responsável, nome referencia
    #usuarios.com
    path('', views.home,name='home'),
    #usuarios.com/usuarios
    path('usuarios/', views.usuario, name="listagem_usuarios"), 
    path('admin/', admin.site.urls)
 ]

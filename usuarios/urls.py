from django.urls import path
from usuarios.views import login, cadastro, pagina_usuario, logout

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('usuario', pagina_usuario, name='pagina_usuario'),
    path('logout', logout, name='logout')
]
from django.urls import path

from django.contrib.auth import views as auth_views

from bases.views import *

app_name = "config"

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='bases/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bases/login.html'), name='logout'),

    # ruta de los usuarios
    path('users-list', UserLis.as_view(), name="users_list"),
    # rutas para modificar usuarios
    path('users-add', user_admin, name="user_add"),
    path('users-modify/<int:pk>', user_admin, name="user_modify"),


    path('catalogos/categorias', Home.as_view(), name='categorias'),
    path('catalogos/subcategorias', Home.as_view(), name='subcategorias'),
    path('movimientos/compras', Home.as_view(), name='compras'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('jogos/reddead1/', views.jogo_reddead1, name='jogo_reddead1'),
    path('jogos/reddead2/', views.jogo_reddead2, name='jogo_reddead2'),
    path('jogos/<int:jogo_id>/', views.detalhes_jogo, name='detalhes_jogo'),
]
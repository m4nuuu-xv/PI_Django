
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('agendar/', views.agendar, name='agendar'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('perfil/', views.perfil, name='perfil'),
]

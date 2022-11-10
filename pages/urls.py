from django.urls import path
from . import views

urlpatterns = [
    path('site/', views.site_view),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('recuperar', views.recuperar_view, name='recuperar'),
    path('registrar', views.registrar_view, name='registrar'),
    path('logout', views.logout_view, name='logout'),
]


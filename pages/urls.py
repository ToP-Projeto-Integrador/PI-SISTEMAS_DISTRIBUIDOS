from django.urls import path
from . import views

urlpatterns = [
    path('', views.ladingpage),
    path('login/', views.login_view),
]

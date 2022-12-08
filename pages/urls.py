from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('site/', views.site_view),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('profile/', views.profile, name='profile'),
    path('recuperar', views.recuperar_view, name='recuperar'),
    path('registrar', views.registrar_view, name='registrar'),
    path('logout', views.logout_view, name='logout'),
    path('config', views.admin_view, name='config'),
    path('config/registrar', views.registrar_view, name='registrar'),
    path('config/backup',  views.backup_view, name="backup"),

    path('createsuperuser/', views.createsuperuser, name='cusers'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render


def site_view(request):
    return render(request, 'site.html')


def home_view(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login/loginpage.html')

    elif request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            return HttpResponse("Tente novamente")


def recuperar_view(request):
    if request.method == 'GET':
        return render(request, 'login/recuperarsenha.html')

    if request.method == 'POST':
        pass


def registrar_view(request):
    if request.method == 'GET':
        return render(request, 'login/registrar.html')

    if request.method == 'POST':
        pass


def logout_view(request):
    logout(request)
    return redirect('login')


def createsuperuser(request):
    if request.method == 'GET':
        user = User.objects.create_superuser(
            username='admin', password='admin')
        user.save()
    return redirect('admin')

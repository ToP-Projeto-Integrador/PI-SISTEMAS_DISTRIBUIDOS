import csv

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import UploadFileForm


def site_view(request):
    return render(request, 'site.html')


def home(request):
    return render(request, 'home.html')

def form(request):
    return render(request, 'form.html')

def profile(request):
    return render(request, 'profile.html')


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


def logout_view(request):
    logout(request)
    return redirect('login')


def admin_view(request):
    return render()


def registrar_view(request):
    if request.method == 'GET':
        return render(request, 'config/registrar.html')

    if request.method == 'POST':
        pass


def backup_view(request):
    if request.method == 'GET':
        return render(request, 'config/backup.html')

    elif request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = form.save()

        # with open(file, newline='') as csvfile:
        #     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        #     for row in spamreader:
        #         print(', '.join(row))
        return render(request, 'config/backup.html')


def createsuperuser(request):
    if request.method == 'GET':
        user = User.objects.create_superuser(
            username='admin', password='admin')
        user.save()
    return redirect('admin')

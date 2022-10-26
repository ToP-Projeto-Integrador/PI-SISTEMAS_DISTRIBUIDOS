from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login


def ladingpage(request):
    return render(request, 'landing.html')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login/loginpage.html')

    elif request.method == 'POST':
        print(request.POST.get('login'), ' ', request.POST.get('password'))
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("LOGOU")
        else:
            return HttpResponse("deslogou")
        return render(request, '/')

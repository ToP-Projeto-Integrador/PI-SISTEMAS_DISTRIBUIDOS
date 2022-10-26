from django.http import HttpResponse
from django.shortcuts import render

def ladingpage(request):
    return render(request, 'landing.html')


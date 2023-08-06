from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')

def gallery(request):
    return render(request, 'mainapp/gallery.html')

def faq(request):
    return render(request, 'mainapp/faq.html')

def about(request):
    return render(request, 'mainapp/about.html')

def login(request):
    return render(request, 'mainapp/login.html')

def register(request):
    return render(request, 'mainapp/register.html')
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

@login_required
def index(request):
    user = User.objects.get(username=request.user)
    context = {
        'user': user,
    }
    return render(request, 'students/index.html', context)

@login_required
def election(request):
    user = User.objects.get(username=request.user)
    context = {
        'user': user,
    }
    return render(request,'students/election.html')

@login_required
def advert(request):
    user = User.objects.get(username=request.user)
    context = {
        'user': user,
    }
    return render(request,'students/adverts.html')

@login_required
def events(request):
    user = User.objects.get(username=request.user)
    context = {
        'user': user,
    }
    return render(request,'students/events.html')

@login_required
def issues(request):
    user = User.objects.get(username=request.user)
    context = {
        'user': user,
    }
    return render(request,'students/issues.html')

@login_required
def payments(request):
    user = User.objects.get(username=request.user)
    context = {
        'user': user,
    }
    return render(request,'students/payment.html')

@login_required
def users_profiles(request):
    user = User.objects.get(username=request.user)
    context = {
        'user': user,
    }
    return render(request,'students/users-profile.html')
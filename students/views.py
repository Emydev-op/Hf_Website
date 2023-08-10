from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

@login_required
def index(request):
    return render(request, 'students/index.html')

@login_required
def election(request):
    return render(request,'students/election.html')

@login_required
def advert(request):
    return render(request,'students/adverts.html')

@login_required
def events(request):
    return render(request,'students/events.html')

@login_required
def issues(request):
    return render(request,'students/issues.html')

@login_required
def payments(request):
    return render(request,'students/payment.html')

@login_required
def users_profiles(request):
    return render(request,'students/users-profiles.html')
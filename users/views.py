from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.roomId = form.cleaned_data.get('roomId')
            user.profile.phoneNo = form.cleaned_data.get('phoneNo')
            user.first_name = form.cleaned_data.get('username')
            user.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('/login')
        else:
            ValueError('Invalid username or password')
            messages.error(request, 'Invalid username or password')
    else:
        messages.error(request, 'Form is not Post')
        form = SignUpForm()
    return render(request, 'mainapp/register.html',{'form': form})

def login(request):
    return render(request, 'mainapp/login.html')

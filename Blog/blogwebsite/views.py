from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def home(request):
    return render(request, 'main.html' )

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

    

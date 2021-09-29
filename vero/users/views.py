from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada: {username}!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request,  'users/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada: {username}!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request,  'users/login.html', {'form': form})

from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.template import RequestContext
from .forms import UserLoginForm, UserRegisterForm
import datetime

# Create your views here.


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('personal_activities_list')
    context = {
        'pageTitle' : 'Register',
    }
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = UserRegisterForm()

    context['form'] = form
    return render(request,  'users/register.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('personal_activities_list')
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return redirect('personal_activities_list')
            response = render(request, "personalActivities/filtroActividadesIndividuales.html")
            response.set_cookie('username', user)
            return response


    else:
        form = UserLoginForm()

    context = {
        'pageTitle' : 'Login',
        'form': form
    }

    return render(request,  'users/login.html', context)

def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

from django import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import eventRegisterForm
from django.contrib.auth.decorators import login_required
from .models import GroupActivity
# Create your views here.


@login_required(login_url='/users/login/')
def index(request):
    context = {
        'pageTitle' : 'CreateEvent',
    }
    if request.method == 'POST':
        form = eventRegisterForm(request.POST)
        if form.is_valid():
            groupActivity = GroupActivity(name = form.cleaned_data["nombre"],       
                                          address = form.cleaned_data["direccion"],
                                          contact = form.cleaned_data.get("email"),
                                          date = form.cleaned_data.get("fecha"),
                                          duration = form.cleaned_data.get("duracion"),
                                          hour = form.cleaned_data.get("hora"),
                                          description = form.cleaned_data.get("descripcion"),
                                          type = form.cleaned_data["tipo"],
                                          creator = request.user
                                          )
          
            groupActivity.save()
            return redirect('index')
            
        else:
            print(form.errors)
            context['form'] = form
            return render(request,  'grupalActivities/grupalActivities.html', context)
    else:
        form = eventRegisterForm()
        context['form'] = form
        return render(request,  'grupalActivities/grupalActivities.html', context)

def myactivity(request):
    return render(request,'grupalActivities/myActivities.html')

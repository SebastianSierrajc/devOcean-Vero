from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    return render(request,'grupalActivities/grupalActivities.html')

def myactivity(request):
    return render(request,'grupalActivities/myActivities.html')

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from encuesta.models import Encuesta

# Create your views here.
def index(request):
  return render(request,"encuesta/encuestaAntes.html")

def encuestaDespues(request):
  return render(request,"encuesta/encuesta.html")

@csrf_exempt
def recibirEncuesta(request):
  #if request.method=="POST" and request.is_ajax():
  #  print(request.POST["sentimientoInicial"])
  #  return JsonResponse({"success": True, "respuesta": "siuu"}, status=200)

  if request.method == 'POST'and request.is_ajax():
    form = Encuesta(request.POST)
    form.save()
  else:
    form = Encuesta()
  return JsonResponse({"success": False, "respuesta": "noou"}, status=400)


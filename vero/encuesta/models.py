import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.


class Encuesta(models.Model):
    sentimientoInicial = models.CharField(max_length=255)
    sentimientoFinal = models.CharField(max_length=255)
    fecha = models.DateTimeField(default=timezone.now)

from django.db import models

# Create your models here.

class Persona(models.Model):
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    edad = models.PositiveBigIntegerField()
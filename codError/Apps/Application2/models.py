from django.db import models

# Create your models here.


class Curso(models.Model):
    nombres = models.CharField(max_length=50)
    creditos = models.PositiveBigIntegerField()
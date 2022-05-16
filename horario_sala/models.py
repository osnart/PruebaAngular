from django.db import models

# Create your models here.
class HoraSala(models.Model):
    #EN AUNTOMATICO GENERA UN id AUTOINCREMENTABLE Y ENTERO
    matricula = models.TextField("Matrícula del Alumno", max_length=50, blank=True)
    nombre = models.TextField("Nombre del Alumno", max_length=50, blank=True)
    sala = models.CharField(" Nombre de la sala", max_length=50, blank=True)
    hora = models.CharField("Hora Alumno", max_length=50, blank=True)

    def __str__(self):
        return self.nombre
        

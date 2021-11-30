from django.db import models

# Create your models here.
class Alumnos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    

    def __str__(self):
        return self.nombre

class Cursos(models.Model):
    nombre = models.CharField(max_length=50)
    alumnos = models.ManyToManyField(Alumnos, through='Asignacion')

    def __str__(self):
        return self.nombre

class Asignacion(models.Model):
    alumnos =  models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()

    def __str__(self):
        return '%s %s'%(self.alumnos, self.cursos)

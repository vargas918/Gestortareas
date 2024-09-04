from django.db import models

# Create your models here.
class Listar(models.Model):
    ESTADO_CHOICES = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )
    titulo = models.CharField(max_length = 100)
    descripcion = models.TextField(max_length = 300)
    estado = models.CharField(max_length=100,choices=ESTADO_CHOICES,default='I')

    def __str__(self):
        return self.titulo
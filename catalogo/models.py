from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    sabor = models.CharField(max_length=100)
    peso = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    activo = models.BooleanField(default=True)
    orden = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} - {self.sabor} - {self.peso}"
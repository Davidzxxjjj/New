from django.db import models

# Create your models here.

class Mascota(models.Model):
    pk_mascota = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    edad = models.CharField(max_length=20, null=False, blank=False)
    raza = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'
        ordering = ['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)

class Cliente(models.Model):
    pk_cliente = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    edad = models.CharField(max_length=50, null=False, blank=False)
    fk_Mascota = models.ForeignKey(Mascota, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)

class Cita(models.Model):
    pk_cita = models.AutoField(primary_key=True, null=False, blank=False)
    fecha = models.DateField(null=False, blank=False)
    fk_Mascota = models.ForeignKey(Mascota, null=False, blank=False, on_delete=models.CASCADE)
    fk_Cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        ordering = ['fecha']

    def __str__(self):
        return "{0}".format(self.fecha)

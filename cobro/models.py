from django.db import models
from decimal import Decimal
from math import ceil

class Cliente(models.Model):
    Nombre = models.CharField(max_length=150)
    Apellido = models.CharField(max_length=150)
    cedula = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"


class Cobro(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="cobros")
    vehiculo = models.CharField(max_length=150)
    placa = models.CharField(max_length=15)
    espacio = models.CharField(max_length=50)
    entrada = models.DateTimeField()
    salida = models.DateTimeField(blank=True, null=True)
    tarifa_por_hora = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.50'))
    total = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = "Cobro de Estacionamiento"
        verbose_name_plural = "Cobros de Estacionamiento"

    def __str__(self):
        return f"{self.vehiculo} ({self.placa}) - {self.espacio}"

    def horas_cobrables(self):
        if not self.salida:
            return 0
        duracion = self.salida - self.entrada
        segundos = duracion.total_seconds()
        return max(1, ceil(segundos / 3600))

    def calcular_total(self):
        return self.tarifa_por_hora * Decimal(self.horas_cobrables())

   



from django.db import models
from .estoque import Estoque

class Demandas(models.Model):
    produto = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.produto} - {self.data} - Quantidade: {self.quantidade}"
    
    class Meta:
        verbose_name = "Demanda"
        verbose_name_plural = "Demandas"
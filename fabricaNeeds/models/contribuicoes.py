from django.db import models

class Contribuinte(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Contribuinte"
        verbose_name_plural = "Contribuintes"



class Contribuicoes(models.Model):
    contribuinte = models.ForeignKey(Contribuinte, on_delete=models.CASCADE)
    contribuicao = models.IntegerField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.contribuinte.nome} - {self.data}"

    
    class Meta:
        verbose_name = "Contribuição"
        verbose_name_plural = "Contribuições"
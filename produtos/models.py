from django.db import models


class Produto(models.Model):
    nome_produto =  models.CharField(max_length=50)
    marca_produto =  models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    foto = models.ImageField(upload_to='produto_foto', null=True, blank=True)

def __str__(self):
        return self.nome_produto + ' ' + self.marca_produto

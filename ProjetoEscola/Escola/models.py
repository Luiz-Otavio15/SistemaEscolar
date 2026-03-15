from django.db import models

# Create your models here.

class TarefaModel(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.TextField(null=True)
    situacao = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome   
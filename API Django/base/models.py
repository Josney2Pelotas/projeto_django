from django.db import models


class Tabela1(models.Model):
    coluna1 = models.IntegerField(blank=True, null=True)
    coluna2 = models.CharField(max_length=64, blank=True, null=True)


class Tabela2(models.Model):
    valor = models.IntegerField(blank=True, null=True)
    tabela1 = models.ForeignKey(Tabela1, blank=True, null=True, on_delete=models.DO_NOTHING)

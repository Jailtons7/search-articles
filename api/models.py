from django.db import models


class TblOrgaoIeExerc(models.Model):
    codSiglaOrgaoIE = models.CharField("Código da IE", max_length=10, primary_key=True)
    nomOrgaoIEExerc = models.CharField("Nome da IE", max_length=50)

    class Meta:
        verbose_name = "Instituição de Ensino de Exercício"
        verbose_name_plural = "Instituições de Ensino de Exercício"

    def __str__(self):
        return f"{self.nomOrgaoIEExerc} - {self.codSiglaOrgaoIE}"

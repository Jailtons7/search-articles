from django.db import models


class TblOrgaoIeExerc(models.Model):
    codSiglaOrgaoIE = models.CharField("Código da IE", max_length=10, primary_key=True)
    nomOrgaoIEExerc = models.CharField("Nome da IE", max_length=50)

    class Meta:
        verbose_name = "Instituição de Ensino de Exercício"
        verbose_name_plural = "Instituições de Ensino de Exercício"

    def __str__(self):
        return f"{self.nomOrgaoIEExerc} - {self.codSiglaOrgaoIE}"


class TblCargos(models.Model):
    CodCargo = models.AutoField(primary_key=True)
    DscCargo = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.DscCargo


class TblServidores(models.Model):
    CodServidor = models.AutoField(primary_key=True)
    CodServidorPortalTransp = models.CharField(max_length=8)
    NomServidor = models.CharField(max_length=60)
    NumCpf = models.CharField(max_length=14)
    NumSiap = models.CharField(max_length=7)
    CodCargo = models.ForeignKey("TblCargos", on_delete=models.CASCADE)
    CodSiglaOrgaoIE = models.ForeignKey("TblOrgaoIeExerc", on_delete=models.CASCADE)

    def __str__(self):
        return self.NomServidor


class TblArtigoPublicado(models.Model):
    pass


class TblProjetos(models.Model):
    pass


class TblEspecialidade(models.Model):
    pass


class TblIndiceJrc2019(models.Model):
    pass


class TblSubArea(models.Model):
    pass


class TblArea(models.Model):
    pass


class TblGrandeArea(models.Model):
    pass


class TblArtigoPublicadoAreaConhecimento(models.Model):
    pass


class TblSituacao(models.Model):
    pass


class TblPalavraChaveArtigo(models.Model):
    pass


class TblArtigoPublicadoPalavraChave(models.Model):
    pass


class TblTitulosArtigos(models.Model):
    pass

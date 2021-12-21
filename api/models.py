from django.db import models


SIM_NAO_OPTIONS = (
    ("SIM", "SIM"),
    ("NAO", "NÂO"),
)


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


class TblIssn(models.Model):
    CodIssn = models.AutoField(primary_key=True)
    DscIssn = models.CharField(max_length=20)
    DscIssnTituloJornal = models.CharField(max_length=195)

    class Meta:
        verbose_name = "ISSN"
        verbose_name_plural = "ISSNs"

    def __str__(self):
        return self.DscIssn


class TblTitulosArtigos(models.Model):
    CodTitulosArtigos = models.AutoField(primary_key=True)
    DscTitulosArtigos = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Titulo de Artigo"
        verbose_name_plural = "Titulos de Artigos"

    def __str__(self):
        return self.DscTitulosArtigos


class TblArtigoPublicado(models.Model):
    CodArtigoPublicado = models.AutoField(primary_key=True)
    ART = models.CharField(max_length=255)
    # ver o que significa o campo ID_ARTIGO na tabela original
    TipArtigoRelevancia = models.CharField(max_length=3, choices=SIM_NAO_OPTIONS)
    TipArtigoDivulgacaoCientifica = models.CharField(max_length=3, choices=SIM_NAO_OPTIONS)
    CodSiglaAtuacaoProfissionalLattes = models.ForeignKey("TblOrgaoIeExerc", on_delete=models.PROTECT)
    CodIssn = models.ForeignKey("TblIssn", on_delete=models.PROTECT)
    CodTitulosArtigos = models.ForeignKey("TblTitulosArtigos", on_delete=models.PROTECT)
    AnoPublicacaoArtigo = models.CharField(max_length=4)

    class Meta:
        verbose_name = "Artigo Publicado"
        verbose_name_plural = "Artigos Publicados"

    def __str__(self):
        return self.get_art()

    def get_art(self) -> str:
        return self.ART[0:40] + "..." if len(self.ART) > 40 else self.ART


class TblProjetos(models.Model):
    pass


class TblIndiceJrc2019(models.Model):
    pass


class TblGrandeArea(models.Model):
    CodGrandeArea = models.AutoField(primary_key=True)
    DscGrandeArea = models.CharField(max_length=27)

    class Meta:
        verbose_name = "Grande Áera"
        verbose_name_plural = "Grandes Áeras"

    def __str__(self):
        return self.DscGrandeArea


class TblArea(models.Model):
    CodGrandeArea = models.ForeignKey("TblGrandeArea", on_delete=models.PROTECT)
    CodArea = models.IntegerField()
    DscArea = models.CharField(max_length=42)

    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"
        constraints = [
            models.UniqueConstraint(fields=["CodGrandeArea", "CodArea"], name="CodGrandeArea_CodArea")
        ]

    def __str__(self):
        return self.DscArea


class TblSubArea(models.Model):
    CodGrandeArea = models.ForeignKey("TblGrandeArea", on_delete=models.PROTECT)
    CodArea = models.ForeignKey("TblArea", on_delete=models.PROTECT)
    CodSubArea = models.IntegerField()
    DscSubArea = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Sub Área"
        verbose_name_plural = "Sub Áreas"
        constraints = [
            models.UniqueConstraint(
                fields=["CodGrandeArea", "CodArea", "CodSubArea"],
                name="CodGrandeArea_CodArea_CodSubArea"
            )
        ]

    def __str__(self):
        return self.DscSubArea


class TblEspecialidade(models.Model):
    CodGrandeArea = models.ForeignKey("TblGrandeArea", on_delete=models.PROTECT)
    CodArea = models.ForeignKey("TblArea", on_delete=models.PROTECT)
    CodSubArea = models.ForeignKey("TblSubArea", on_delete=models.PROTECT)
    CodEspecialidade = models.IntegerField()
    DscEspecialidade = models.CharField(max_length=85)

    class Meta:
        verbose_name = "Sub Área"
        verbose_name_plural = "Sub Áreas"
        constraints = [
            models.UniqueConstraint(
                fields=["CodGrandeArea", "CodArea", "CodSubArea", "CodEspecialidade"],
                name="CodGrandeArea_CodArea_CodSubArea_CodEspecialidade"
            )
        ]

    def __str__(self):
        return self.DscEspecialidade


class TblArtigoPublicadoAreaConhecimento(models.Model):
    pass


class TblSituacao(models.Model):
    pass


class TblPalavraChaveArtigo(models.Model):
    pass


class TblArtigoPublicadoPalavraChave(models.Model):
    pass



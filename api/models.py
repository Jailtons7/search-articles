from django.db import models


SIM_NAO_OPTIONS = (
    ("SIM", "SIM"),
    ("NAO", "NÃO"),
)


class TblOrgaoIeExerc(models.Model):
    CodSiglaOrgaoIE = models.CharField("Código da IE", max_length=10, primary_key=True)
    NomOrgaoIEExerc = models.CharField("Nome da IE", max_length=50)

    class Meta:
        verbose_name = "Instituição de Ensino de Exercício"
        verbose_name_plural = "Instituições de Ensino de Exercício"

    def __str__(self):
        return f"{self.NomOrgaoIEExerc} - {self.CodSiglaOrgaoIE}"


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
    AnoPublicacaoArtigo = models.CharField(max_length=4, db_index=True)

    CodSiglaAtuacaoProfissionalLattes = models.ForeignKey("TblOrgaoIeExerc", on_delete=models.PROTECT)
    CodIssn = models.ForeignKey("TblIssn", on_delete=models.PROTECT)
    CodTitulosArtigos = models.ForeignKey("TblTitulosArtigos", on_delete=models.PROTECT)
    CodIdioma = models.ForeignKey("TblIdioma", on_delete=models.SET_NULL, null=True)
    CodServidor = models.ForeignKey("TblServidores", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Artigo Publicado"
        verbose_name_plural = "Artigos Publicados"

    def __str__(self):
        return self.get_art()

    def get_art(self) -> str:
        return self.ART[0:40] + "..." if len(self.ART) > 40 else self.ART


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
    CodArea = models.AutoField(primary_key=True)
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
    CodSubArea = models.AutoField(primary_key=True)
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
    CodEspecialidade = models.AutoField(primary_key=True)
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
    CodArtigoPublicado = models.ForeignKey("TblArtigoPublicado", on_delete=models.PROTECT)
    CodGrandeArea = models.ForeignKey("TblGrandeArea", on_delete=models.PROTECT)
    CodArea = models.ForeignKey("TblArea", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Artigo publicado por área do conhecimento"
        verbose_name_plural = "Artigos publicados por área do conhecimento"

    def __str__(self):
        return f"{self.CodArtigoPublicado.CodTitulosArtigos.DscTitulosArtigos[:25]} -> " \
               f"{self.CodGrandeArea.DscGrandeArea}"


class TblSituacao(models.Model):
    CodSituacao = models.AutoField(primary_key=True)
    DscSituacao = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Situação"
        verbose_name_plural = "Situações"

    def __str__(self):
        return self.DscSituacao


class TblPalavraChaveArt(models.Model):
    CodPalavrasChavesArtigos = models.AutoField(primary_key=True)
    DscArtigoPalavrasChave = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Plavra chave"
        verbose_name_plural = "Plavras chaves"

    def __str__(self):
        return self.DscArtigoPalavrasChave


class TblArtigoPublicadoPalavrasChave(models.Model):
    CodArtigoPublicado = models.ForeignKey("TblArtigoPublicado", on_delete=models.PROTECT)
    CodPalavrasChavesArtigos = models.ForeignKey("TblPalavraChaveArt", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Artigo Publicado - Palavra-Chave"
        verbose_name_plural = "Artigos Publicados - Palavras-Chaves"

    def __str__(self):
        return f"{self.CodArtigoPublicado.CodIssn} - {self.CodPalavrasChavesArtigos.DscArtigoPalavrasChave}"


class TblIdioma(models.Model):
    CodIdioma = models.AutoField(primary_key=True)
    DscIdioma = models.CharField(max_length=15)

    def __str__(self):
        return self.DscIdioma

    class Meta:
        verbose_name = "Idioma"
        verbose_name_plural = "Idiomas"

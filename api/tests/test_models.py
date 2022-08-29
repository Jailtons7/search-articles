from django.test import TestCase

from api.models import (
    TblCargos, TblOrgaoIeExerc, TblServidores, TblArtigoPublicado, TblArtigoPublicadoPalavrasChave,
    TblIssn, TblTitulosArtigos, TblIdioma, TblArtigoPublicadoAreaConhecimento, TblGrandeArea, TblArea,
    SIM_NAO_OPTIONS,
)


class TestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        Create data before run all tests
        """
        cargo_servidor = cls.cargo_servidor = TblCargos.objects.create(CodCargo=1, DscCargo='Servidor')
        cargo_professor = cls.cargo_professor = TblCargos.objects.create(CodCargo=2, DscCargo='Professor')
        ie1 = cls.ie1 = TblOrgaoIeExerc.objects.create(CodSiglaOrgaoIE='ORG1', NomOrgaoIEExerc='Org. Teste 1')
        ie2 = cls.ie2 = TblOrgaoIeExerc.objects.create(CodSiglaOrgaoIE='ORG2', NomOrgaoIEExerc='Org. Teste 2')
        cls.servidor = TblServidores.objects.create(
            CodServidor=1, CodServidorPortalTransp='1', NomServidor='Ana', NumCpf='12345678912',
            NumSiap='1', CodCargo=cargo_servidor, CodSiglaOrgaoIE=ie1
        )
        professor = cls.professor = TblServidores.objects.create(
            CodServidor=2, CodServidorPortalTransp='2', NomServidor='José', NumCpf='12345678934',
            NumSiap='2', CodCargo=cargo_professor, CodSiglaOrgaoIE=ie2
        )
        issn = cls.issn = TblIssn.objects.create(
            CodIssn=1, DscIssn='Issn teste', DscIssnTituloJornal='Título teste'
        )
        titulo_art = cls.titulo_art = TblTitulosArtigos.objects.create(
            CodTitulosArtigos=1, DscTitulosArtigos='Título teste'
        )
        idioma = cls.idioma = TblIdioma.objects.create(
            CodIdioma=1, DscIdioma="Inglês"
        )
        artigo_pub_1 = cls.artigo_pub = TblArtigoPublicado.objects.create(
            CodArtigoPublicado=1, ART='art. teste', TipArtigoRelevancia=SIM_NAO_OPTIONS[0][0],
            TipArtigoDivulgacaoCientifica=SIM_NAO_OPTIONS[0][0], AnoPublicacaoArtigo='2022',
            CodSiglaAtuacaoProfissionalLattes=ie1, CodIssn=issn, CodTitulosArtigos=titulo_art,
            CodIdioma=idioma, CodServidor=professor
        )
        grande_area = cls.grande_area = TblGrandeArea.objects.create(
            CodGrandeArea=1, DscGrandeArea="Grande Area"
        )
        area = cls.area = TblArea.objects.create(CodGrandeArea=grande_area, CodArea=1, DscArea="Area")
        art_pub_area_conhec = cls.art_pub_area_conhec = TblArtigoPublicadoAreaConhecimento.objects.create(
            CodArtigoPublicado=artigo_pub_1, CodGrandeArea=grande_area, CodArea=area
        )

    def test_servidores_per_ie(self):
        serv_per_ie = TblServidores.servidores_per_ie()
        self.assertEqual(len(serv_per_ie), 2)
        self.assertEqual(list(serv_per_ie), [('ORG1', 1), ('ORG2', 1)])

    def test_professores_per_ie(self):
        prof_per_ie = TblServidores.professores_per_ie()
        self.assertEqual(len(prof_per_ie), 1)
        self.assertEqual(list(prof_per_ie), [('ORG2', 1)])

    def test_articles_per_grande_area(self):
        articles_per_grande_area = TblArtigoPublicadoAreaConhecimento.articles_per_grande_area()
        self.assertEqual(len(articles_per_grande_area), 1)
        self.assertEqual(list(articles_per_grande_area), [('Grande Area', 1)])

    def test_articles_per_orgao(self):
        articles_per_orgao = TblArtigoPublicado.articles_per_orgao()
        self.assertEqual(len(articles_per_orgao), 1)
        self.assertEqual(list(articles_per_orgao), [('ORG2', 1)])

    def test_articles_per_year(self):
        articles_per_year = TblArtigoPublicado.articles_per_year()
        self.assertEqual(len(articles_per_year), 1)
        self.assertEqual(list(articles_per_year), [('2022', 1)])

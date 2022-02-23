from django.test import TestCase

from api.models import (
    TblCargos, TblOrgaoIeExerc, TblServidores
)


class TestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        cargo_servidor = cls.cargo_servidor = TblCargos.objects.create(CodCargo=1, DscCargo='Servidor')
        cargo_professor = cls.cargo_professor = TblCargos.objects.create(CodCargo=2, DscCargo='Professor')
        ie1 = cls.ie1 = TblOrgaoIeExerc.objects.create(CodSiglaOrgaoIE='ORG1', NomOrgaoIEExerc='Org. Teste 1')
        ie2 = cls.ie2 = TblOrgaoIeExerc.objects.create(CodSiglaOrgaoIE='ORG2', NomOrgaoIEExerc='Org. Teste 2')
        cls.servidor = TblServidores.objects.create(
            CodServidor=1, CodServidorPortalTransp='1', NomServidor='Ana', NumCpf='12345678912',
            NumSiap='1', CodCargo=cargo_servidor, CodSiglaOrgaoIE=ie1
        )
        cls.professor = TblServidores.objects.create(
            CodServidor=2, CodServidorPortalTransp='2', NomServidor='José', NumCpf='12345678934',
            NumSiap='2', CodCargo=cargo_professor, CodSiglaOrgaoIE=ie2
        )

    def test_servidores_per_ie(self):
        serv_per_ie = TblServidores.servidores_per_ie()
        self.assertEqual(len(serv_per_ie), 2)
        self.assertEqual(list(serv_per_ie), [('ORG1', 1), ('ORG2', 1)])

    def test_professores_per_ie(self):
        prof_per_ie = TblServidores.professores_per_ie()
        self.assertEqual(len(prof_per_ie), 1)
        self.assertEqual(list(prof_per_ie), [('ORG2', 1)])

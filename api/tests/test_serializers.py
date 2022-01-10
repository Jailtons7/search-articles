from django.test import TestCase

from api.serializers import (
    OrgaoIeExercSerializer,
    CargosSerializer,
)


class SerializersTest(TestCase):
    def test_valid_orgao_ie_exerc_serializer(self):
        dict_data = {
            'CodSiglaOrgaoIE': 'UFAL',
            'NomOrgaoIEExerc': 'Universidade Federal de Alagoas'
        }
        serializer = OrgaoIeExercSerializer(
            data={'CodSiglaOrgaoIE': 'UFAL', 'NomOrgaoIEExerc': 'Universidade Federal de Alagoas'}
        )
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, dict_data)
        self.assertEqual(serializer.data, dict_data)

    def test_invalid_orgao_ie_exerc_serializer(self):
        data_none = None
        invalid_data = {
            'CodSiglaOrgaoIE': 'Universidade Federal de Alagoas',  # max_lenght > 10
            'NomOrgaoIEExerc': 'Universidade Federal de Alagoas'
        }
        serializer = OrgaoIeExercSerializer(data=data_none)
        self.assertFalse(serializer.is_valid(), msg="data None must be invalid")
        serializer = OrgaoIeExercSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid(), msg="CodSiglaOrgaoIE must be less than 10")

    def test_valid_cargo_serializer(self):
        dict_data = {
            'DscCargo': 'Professor'
        }
        serializer = CargosSerializer(data=dict_data)
        self.assertTrue(serializer.is_valid(), msg="dict data must be valid")
        self.assertEqual(serializer.validated_data, dict_data, msg="dict data must be equal to validated data")
        self.assertEqual(serializer.data, dict_data, msg="dict data must be equal to serializer data")

    def test_invalid_cargo_serializer(self):
        invalid_data = {
            'DscCargo': 'Professor Universitário Nível 1'  # max_lenght > 20
        }
        data_none = None
        serializer = CargosSerializer(data=data_none)
        self.assertFalse(serializer.is_valid())
        serializer = CargosSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid(), msg="max_lenght of DscCargo must be less than 20")

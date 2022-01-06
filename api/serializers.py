from rest_framework import serializers

from api.models import (
    TblOrgaoIeExerc,
    TblCargos,
    TblServidores,
    TblIdioma,
    TblIssn,
    TblTitulosArtigos,
    TblArtigoPublicado,
)


class OrgaoIeExercSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblOrgaoIeExerc
        fields = ('CodSiglaOrgaoIE', 'NomOrgaoIEExerc')


class CargosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblCargos
        fields = ('CodCargo', 'DscCargo')


class ServidoresSerializer(serializers.ModelSerializer):
    CodCargo = CargosSerializer()
    CodSiglaOrgaoIE = OrgaoIeExercSerializer()

    class Meta:
        model = TblServidores
        fields = (
            'CodServidor', 'CodServidorPortalTransp', 'NomServidor',
            'NumCpf', 'NumSiap', 'CodCargo', 'CodSiglaOrgaoIE'
        )


class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblIdioma
        fields = ('CodIdioma', 'DscIdioma')


class IssnSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblIssn
        fields = ('CodIssn', 'DscIssn', 'DscIssnTituloJornal')


class TitulosArtigosSerilizer(serializers.ModelSerializer):
    class Meta:
        model = TblTitulosArtigos
        fields = ('CodTitulosArtigos', 'DscTitulosArtigos')


class ArtigoPublicadoSerializer(serializers.ModelSerializer):
    CodSiglaAtuacaoProfissionalLattes = OrgaoIeExercSerializer()
    CodIssn = IssnSerializer()
    CodTitulosArtigos = TitulosArtigosSerilizer()
    CodIdioma = IdiomaSerializer()
    CodServidor = ServidoresSerializer()

    class Meta:
        model = TblArtigoPublicado
        fields = (
            'CodArtigoPublicado', 'ART', 'TipArtigoRelevancia', 'TipArtigoDivulgacaoCientifica',
            'AnoPublicacaoArtigo', 'CodSiglaAtuacaoProfissionalLattes', 'CodIssn', 'CodTitulosArtigos',
            'CodIdioma', 'CodServidor'
        )

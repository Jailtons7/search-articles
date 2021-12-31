import json

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import IntegrityError, models

from api.models import (
    TblIssn,
    TblTitulosArtigos,
    TblOrgaoIeExerc,
    TblCargos,
    TblGrandeArea,
    TblPalavraChaveArt,
    TblArtigoPublicado,
    TblServidores,
    TblArea,
    TblArtigoPublicadoPalavrasChave,
    TblArtigoPublicadoAreaConhecimento,
    TblSubArea,
    TblEspecialidade,
)


class Command(BaseCommand):
    @staticmethod
    def json_to_dict(file_name: str) -> dict:
        file_path = f'{str(settings.BASE_DIR)}/api/fixtures/{file_name}'
        with open(file_path) as f:
            dic = json.load(f)
            return dic

    def insert_data_to_model(self, model: models.Model, dict_data: dict):
        try:
            model.objects.create(**dict_data)
        except IntegrityError:
            self.stdout.write(f'{model._meta.object_name} was already populated')

    def add_arguments(self, parser):
        parser.add_argument('--model', action='append', type=str)
        parser.add_argument('--foregeign_key', action='append', nargs='+', type=str)

    def handle(self, *args, **options):
        self.stdout.write('Starting data upload')
        dict_issn = self.json_to_dict('TblIssn.json')
        for data in dict_issn:
            self.insert_data_to_model(model=TblIssn, dict_data=data)
        del dict_issn

        article_titles = self.json_to_dict('TblTitulosArtigos.json')
        for data in article_titles:
            self.insert_data_to_model(model=TblTitulosArtigos, dict_data=data)
        del article_titles

        ie_exercicio = self.json_to_dict('TblOrgaoIeExerc.json')
        for data in ie_exercicio:
            self.insert_data_to_model(model=TblOrgaoIeExerc, dict_data=data)
        del ie_exercicio

        cargos = self.json_to_dict('TblCargos.json')
        for data in cargos:
            self.insert_data_to_model(model=TblCargos, dict_data=data)
        del cargos

        grande_area = self.json_to_dict('TblGrandeArea.json')
        for data in grande_area:
            self.insert_data_to_model(model=TblGrandeArea, dict_data=data)
        del grande_area

        palavra_chave_artigo = self.json_to_dict('TblPalavraChaveArt.json')
        for data in palavra_chave_artigo:
            self.insert_data_to_model(model=TblPalavraChaveArt, dict_data=data)
        del palavra_chave_artigo

        artigo_publicado = self.json_to_dict('TblArtigoPublicado.json')
        for data in artigo_publicado:
            self.insert_data_to_model(model=TblArtigoPublicado, dict_data=data)
        del artigo_publicado

        servidores = self.json_to_dict('TblServidores.json')
        for data in servidores:
            self.insert_data_to_model(model=TblServidores, dict_data=data)
        del servidores

        area = self.json_to_dict('TblArea.json')
        for data in area:
            self.insert_data_to_model(model=TblArea, dict_data=data)
        del area

        art_publ_palavra_chave = self.json_to_dict('TblArtigoPublicadoPalavrasChave.json')
        for data in art_publ_palavra_chave:
            self.insert_data_to_model(model=TblArtigoPublicadoPalavrasChave, dict_data=data)
        del art_publ_palavra_chave

        art_publ_area_conhecimento = self.json_to_dict('TblArtigoPublicadoAreaConhecimento.json')
        for data in art_publ_area_conhecimento:
            self.insert_data_to_model(model=TblArtigoPublicadoAreaConhecimento, dict_data=data)
        del art_publ_area_conhecimento

        subarea = self.json_to_dict('TblSubArea.json')
        for data in subarea:
            self.insert_data_to_model(model=TblSubArea, dict_data=data)
        del subarea

        especialidade = self.json_to_dict('TblEspecialidade.json')
        for data in especialidade:
            self.insert_data_to_model(model=TblEspecialidade, dict_data=data)
        self.stdout.write('Data upload is finished')

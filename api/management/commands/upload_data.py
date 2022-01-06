import sys
import json

from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError, models


class Command(BaseCommand):
    help = """
    Populates database passed in --model option.
    
    To each model you want to populate,
    you should provide a json file in PROJECT_ROOT/api/fixtures/.
    """

    @staticmethod
    def json_to_dict(file_name: str) -> dict:
        file_path = f'{str(settings.BASE_DIR)}/api/fixtures/{file_name}'
        with open(file_path) as f:
            dic = json.load(f)
            return dic

    @staticmethod
    def modify_data(d: dict, fks: list, not_used: list = []):
        """
        Avoid adding an object in foreign keys
        """
        for value in fks:
            d[f'{value}_id'] = d[value]
            del d[value]

        for value in not_used:
            del d[value]

    def insert_data_to_model(self, model: models.Model, dict_data: dict):
        try:
            model.objects.create(**dict_data)
        except IntegrityError:
            self.stdout.write(f'{model._meta.object_name}: Integrity issue with data {dict_data}')

    def add_arguments(self, parser):
        parser.add_argument('-m', '--model', type=str)
        parser.add_argument('-f', '--foregeign_key', action='append', nargs='+', type=str)
        parser.add_argument('-n', '--not_use', action='append', nargs='+', type=str)

    def handle(self, *args, **options):
        model_nm = options.get('model')
        list_fkeys = options.get('foregeign_key')
        not_used_fields = options.get('not_use') or [[]]

        if model_nm is None:
            raise CommandError("--model argument is required")

        all_models = apps.all_models['api'].keys()
        if model_nm.lower() not in all_models:
            raise CommandError("Please, provide a valid model name.")

        self.stdout.write(self.style.SUCCESS('Starting data upload'))
        self.stdout.write(self.style.WARNING('It may take a couple of minutes.'))
        try:
            model = getattr(sys.modules['api.models'], model_nm)
        except AttributeError:
            raise CommandError(f"{model_nm} is not a valid model. Tip: The --model option is case sensitive.")

        data_madel = self.json_to_dict(f'{model.__name__}.json')
        for data in data_madel:
            if list_fkeys:
                fkeys = list_fkeys[0]
                self.modify_data(data, fkeys, not_used_fields[0])
            self.insert_data_to_model(model=model, dict_data=data)

        self.stdout.write(self.style.SUCCESS(f'Added data to {model.__name__} successfully'))

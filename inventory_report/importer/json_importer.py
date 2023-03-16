from inventory_report.importer.importer import Importer
import os
import json


class JsonImporter(Importer):
    @staticmethod
    def check_file_format(file_path):
        # https://www.delftstack.com/pt/howto/python/python-get-file-extension/

        # os.path.splitext(file_path) retorna:
        # ('inventory_report/data/inventory', '.csv')
        extension = os.path.splitext(file_path)
        return extension[1]

    @classmethod
    def import_data(cls, file_path):
        extension = cls.check_file_format(file_path)

        if extension == '.json':
            with open(file_path, encoding='utf-8') as file:
                products = json.load(file)
                return products
        elif extension != '.json':
            raise ValueError("Arquivo inválido")

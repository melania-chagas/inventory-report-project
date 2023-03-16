from inventory_report.importer.importer import Importer
import csv
import os


class CsvImporter(Importer):
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

        if extension == '.csv':
            with open(file_path, 'r') as file:
                csv_file = csv.DictReader(file)
                products = []
                for line in csv_file:
                    products.append(line)
            return products
        elif extension != '.csv':
            raise ValueError("Arquivo inválido")

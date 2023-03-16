from inventory_report.importer.importer import Importer
import os
import xmltodict


class XmlImporter(Importer):
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

        if extension == '.xml':
            # https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/xml.html
            with open(file_path) as file:
                products = xmltodict.parse(file.read())
                # products é um objeto que contém a chave 'dataset'
                # e dentro dela contém a chave 'record', que é onde está a
                # lista de produtos que preciso
                return products['dataset']['record']
        elif extension != '.xml':
            raise ValueError("Arquivo inválido")

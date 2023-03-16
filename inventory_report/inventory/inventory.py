from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import os
import json
import xmltodict


class Inventory:
    @staticmethod
    def generate_report(report_type, products):
        if report_type == "simples":
            return SimpleReport.generate(products)
        if report_type == "completo":
            return CompleteReport.generate(products)

    @staticmethod
    def check_file_format(file_path):
        # https://www.delftstack.com/pt/howto/python/python-get-file-extension/

        # os.path.splitext(file_path) retorna:
        # ('inventory_report/data/inventory', '.csv')
        extension = os.path.splitext(file_path)
        return extension[1]

    @classmethod
    def import_data(cls, file_path, report_type):
        extension = cls.check_file_format(file_path)
        if extension == '.csv':
            with open(file_path, 'r') as file:
                csv_file = csv.DictReader(file)
                products = []
                for line in csv_file:
                    products.append(line)
            return cls.generate_report(report_type, products)
        elif extension == '.json':
            with open(file_path, encoding='utf-8') as file:
                products = json.load(file)
                return cls.generate_report(report_type, products)
        elif extension == '.xml':
            # https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/xml.html
            with open(file_path) as file:
                products = xmltodict.parse(file.read())
                # products é um objeto que contém a chave 'dataset'
                # e dentro dela contém a chave 'record', que é onde está a
                # lista de produtos que preciso
                return cls.generate_report(
                    report_type, products['dataset']['record']
                )


# path = """/home/melania/trybe/projects/sd-022-a-inventory-report/
# inventory_report/data/inventory.xml"""
# print(Inventory.import_data(path, 'completo'))

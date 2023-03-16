from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import os


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


# path = """
# /home/melania/trybe/projects/sd-022-a-inventory-report/inventory_report/data/inventory.csv"""
# print(Inventory.import_data(path, 'completo'))

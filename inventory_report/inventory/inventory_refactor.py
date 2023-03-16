from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    @staticmethod
    def generate_report(report_type, products):
        if report_type == "simples":
            return SimpleReport.generate(products)
        if report_type == "completo":
            return CompleteReport.generate(products)

    def import_data(self, file_path, report_type):
        self.data += self.importer.import_data(file_path)
        self.generate_report(report_type, self.data)

    def __iter__(self):
        return InventoryIterator(self.data)

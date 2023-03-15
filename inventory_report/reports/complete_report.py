# import json
from collections import Counter
from inventory_report.reports.simple_report import SimpleReport
# import simple_report
# simple_report = simple_report.SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def get_number_of_products(dict_list):
        list_of_companies = []
        for company in dict_list:
            list_of_companies.append(company["nome_da_empresa"])
        number_of_products_by_company = Counter(list_of_companies)
        result = []
        for index in number_of_products_by_company:
            name_and_quantity = index, number_of_products_by_company[index]
            result.append(
                f'- {name_and_quantity[0]}: {name_and_quantity[1]}\n'
            )
        return result

    @classmethod
    def generate(self, dict_list):
        simple_report = super().generate(dict_list)
        number_of_products_by_company = self.get_number_of_products(dict_list)
        return f"""{simple_report}\nProdutos estocados por empresa:
{''.join(number_of_products_by_company)}"""


# with open("inventory_report/data/inventory.json", encoding='utf-8') as json_:
#     data = json.load(json_)


# print(CompleteReport.generate(data))

import json
import collections


class SimpleReport:
    @classmethod
    def generate(cls, dict_list):
        manufacture_list = []
        validity_list = []
        list_of_companies = []

        for item in dict_list:
            manufacture_list.append(item["data_de_fabricacao"])
            validity_list.append(item["data_de_validade"])
            list_of_companies.append(item["nome_da_empresa"])

        manufacture_list.sort()
        validity_list.sort()

        oldest_manufacture = manufacture_list[0]
        next_due_date = validity_list[0]
        # https://docs.python.org/pt-br/3/library/collections.html
        counter = collections.Counter()
        for company in list_of_companies:
            counter[company] += 1
        greater_quantity_of_products = list(counter.keys())[0]

        return (
            f"Data de fabricação mais antiga: {oldest_manufacture}\n"
            f"Data de validade mais próxima: {next_due_date}\n"
            f"Empresa com mais produtos: {greater_quantity_of_products}\n"
        )


# with open("inventory_report/data/inventory.json", encoding='utf-8') as json_:
#     data = json.load(json_)

# print(SimpleReport.generate(data))

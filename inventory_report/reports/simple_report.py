# import json
from collections import Counter
from datetime import date


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
        unexpired_dates_in_validity_list = []
        today = date.today()
        for date_ in validity_list:
            if date_ > str(today):
                unexpired_dates_in_validity_list.append(date_)
        unexpired_dates_in_validity_list.sort()

        oldest_manufacture = manufacture_list[0]
        next_due_date = unexpired_dates_in_validity_list[0]
        # https://docs.python.org/pt-br/3/library/collections.html
        result = Counter(list_of_companies)
        print(result.most_common(1)[0])
        greater_quantity_of_products = result.most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_manufacture}\n"
            f"Data de validade mais próxima: {next_due_date}\n"
            f"Empresa com mais produtos: {greater_quantity_of_products}"
        )


# with open("inventory_report/data/inventory.json", encoding='utf-8') as json_:
#     data = json.load(json_)

# print(SimpleReport.generate(data))

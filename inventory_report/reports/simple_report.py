# import json
from collections import Counter
from datetime import date


class SimpleReport:
    @staticmethod
    def get_oldest_manufacture(dict_list):
        manufacture_list = []

        for item in dict_list:
            manufacture_list.append(item["data_de_fabricacao"])

        manufacture_list.sort()
        return manufacture_list[0]

    @staticmethod
    def get_next_due_date(dict_list):
        expiration_date = []

        for item in dict_list:
            expiration_date.append(item["data_de_validade"])

        unexpired_date_list = []
        today = date.today()
        for date_ in expiration_date:
            if date_ > str(today):
                unexpired_date_list.append(date_)
        unexpired_date_list.sort()

        return unexpired_date_list[0]

    @staticmethod
    def get_greater_quantity_of_products(dict_list):
        list_of_companies = []

        for item in dict_list:
            list_of_companies.append(item["nome_da_empresa"])

        result = Counter(list_of_companies)

        # 'result.most_common(1)' retorna: [('Target Corporation', 4)]
        # 'result.most_common(1)[0]' retorna: ('Target Corporation', 4)
        # 'result.most_common(1)[0][0]' retorna: Target Corporation
        return result.most_common(1)[0][0]

    @classmethod
    def generate(cls, dict_list):
        return (
            "Data de fabricação mais antiga: "
            f"{cls.get_oldest_manufacture(dict_list)}\n"
            "Data de validade mais próxima: "
            f"{cls.get_next_due_date(dict_list)}\n"
            f"Empresa com mais produtos: "
            f"{cls.get_greater_quantity_of_products(dict_list)}"
        )


# with open("inventory_report/data/inventory.json", encoding='utf-8') as json_:
#     data = json.load(json_)

# print(SimpleReport.generate(data))

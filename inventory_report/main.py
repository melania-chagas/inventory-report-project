from inventory_report.inventory.inventory import Inventory
import sys


def main():
    # https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/290e715d-73e3-4b2d-a3c7-4fe113474070/section/b436f9e0-dfde-4a16-9bad-82f0c559dd45/day/61e88b4a-b97a-4f96-b5a0-abaa50651e37/lesson/af7e97a4-654f-47c1-a3e8-f726ee91960f

    # https://www.pythonforbeginners.com/system/python-sys-argv
    # https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/
    try:
        _, file_path, report_type = sys.argv

        report = Inventory.import_data(file_path, report_type)
        # stdout - recebe informações regulares do programa
        sys.stdout.write(report)
    except ValueError:
        # stderr - imprime apenas exceções e mensagens de erro
        sys.stderr.write('Verifique os argumentos\n')

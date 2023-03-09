from inventory_report.inventory.product import Product


def test_cria_produto():
    # Testa o método __init__ da classe 'Product'

    product = Product(
        1,
        "Nicotine Polacrilex",
        "Target Corporation",
        "2021-02-18",
        "2023-09-17",
        "CR25 1551 4467 2549 4402 1",
        "instrucao 1"
    )

    assert product.id == 1
    assert product.nome_do_produto == "Nicotine Polacrilex"
    assert product.nome_da_empresa == "Target Corporation"
    assert product.data_de_fabricacao == "2021-02-18"
    assert product.data_de_validade == "2023-09-17"
    assert product.numero_de_serie == "CR25 1551 4467 2549 4402 1"
    assert product.instrucoes_de_armazenamento == "instrucao 1"

    assert type(product.id) is int
    assert type(product.nome_do_produto) is str
    assert type(product.nome_da_empresa) is str
    assert type(product.data_de_fabricacao) is str
    assert type(product.data_de_validade) is str
    assert type(product.numero_de_serie) is str
    assert type(product.instrucoes_de_armazenamento) == str

from carrinho import Produto, CarrinhoDeCompras
import pytest

@pytest.fixture
def carrinho_cheio():
    print("Montando carrinho com produtos de teste")
    carrinho = CarrinhoDeCompras()

    produto1 = Produto(nome="Notebook", preco=3000)
    produto2 = Produto(nome="Teclado", preco=500)

    carrinho.adicionar_produto(produto1)
    carrinho.adicionar_produto(produto2)
    print(f"Carrinho preparado com {len(carrinho.produtos)} produtos")
    return carrinho


def test_calcular_total_sem_desconto(carrinho_cheio):
    total_carrinho = carrinho_cheio.calcular_total()
    print(f"Total sem desconto: {total_carrinho}")
    assert total_carrinho == 3500


@pytest.mark.parametrize("valor_desconto, valor_esperado_carrinho", 
                         [(10, 3150), (20, 2800), (50, 1750)])
def test_calcular_total_com_desconto(carrinho_cheio, valor_desconto, valor_esperado_carrinho):
    total_carrinho = carrinho_cheio.calcular_total(desconto_percentual=valor_desconto)
    print(f"Desconto de {valor_desconto}% gerou total {total_carrinho}")
    assert total_carrinho == valor_esperado_carrinho
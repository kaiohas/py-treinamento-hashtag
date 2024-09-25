#F - Falha
#E - Exceção/Erro
#. - correto


from main import calcular_lucro, calcular_faturamento, calcular_custo
import pytest

def test_calcular_lucro():
    faturamento = calcular_faturamento()
    assert calcular_lucro(faturamento,500)>0

@pytest.mark.faturamento
def test_calcular_faturamento():
    assert type(calcular_faturamento()) == int

@pytest.fixture
def cotacao():
    return 5

def test_calcular_custo(cotacao):
    assert calcular_custo(cotacao) > 0
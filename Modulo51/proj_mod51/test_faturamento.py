#F - Falha
#E - Exceção/Erro
#. - correto


from main import calcular_faturamento
import pytest


@pytest.mark.faturamento
def test_calcular_faturamento():
    assert (calcular_faturamento()) > 0
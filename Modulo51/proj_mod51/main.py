

def calcular_custo(cotacao):
    custo = 1000 * cotacao
    return custo

def calcular_faturamento():
    vendas = [10,20,30,40,500]
    faturamento = sum(vendas)
    return faturamento

def calcular_lucro(faturamento,custo):
    lucro = faturamento - custo
    return lucro



from random import randint
class Agencia:

    def __init__(self,telefone,cnpj,numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero  = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nível recomendado. Caixa atual: {self.caixa}')
        else:
            print(f'O valor do caixa está ok. Caixa atual: {self.caixa}')

    def emprestar_dinheiro(self,valor,cpf,juros):
        if self.caixa > valor:
            self.emprestimos.append((valor,cpf,juros))
        else:
            print("Emprestimo não é possível")

    def adicionar_cliente(self,nome,cpf,patrimonio):
        self.clientes.append((nome,cpf,patrimonio))


class AgenciaVirtual(Agencia):

    def __init__(self,site,telefone,cnpj):

        self.site = site
        super().__init__(telefone,cnpj,105)
        self.caixa = 10000000
        self.caixa_paypal = 0

    def depositar_paypal(self,valor):
        self.caixa -= valor
        self.caixa_paypal +=valor

    def sacar_paypal(self):
        self.caixa += valor
        self.caixa_paypal -=valor

class AgenciaComum(Agencia):

    def __init__(self,telefone,cnpj):
        super().__init__(telefone,cnpj,numero=randint(1000,9999))
        self.caixa = 100000

class AgenciaPremium(Agencia):

    def __init__(self,telefone,cnpj):
        super().__init__(telefone,cnpj,numero=randint(1000,9999))
        self.caixa = 100000000

    def adicionar_cliente(self,nome,cpf,patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome,cpf,patrimonio)
        else:
            print("O cliente não tem o patrimonio necessário para entrar na agencia premium")



if __name__ == '__main__':

    agencia1 = Agencia(222555555,214124124,2255)

    agencia1.caixa = 10000000
    agencia1.verificar_caixa()

    agencia1.emprestar_dinheiro(1500,1231251512,0.02)

    print(agencia1.emprestimos)

    agencia1.adicionar_cliente('kaio',123124151,1000000)

    print(agencia1.clientes)
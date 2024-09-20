import time
from datetime import datetime
import pytz
from random import randint
class ContaCorrente:

    """
    Cria um objeto conta corrente para gerenciar a conta dos clientes.

    Atributos:
    Nome(str): Nome do cliente
    CPF(str): Cpf do cliente
    Agencia(int): Agencia responsável pela conta do cliente.
    conta(int): numero da conta do cliente.
    saldo(int): Saldo do cliente.
    limite: limite de gasto do cliente.

    """

    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%Y %H:%M:%S')


    def __init__(self,nome, cpf,agencia,num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        """
        Retorna o saldo da conta do participante.
        :return: print do saldo
        """
        print(f'Seu saldo atual é de: R${self._saldo:.2f}')

    def depositar(self,valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self,valor):
        if self._saldo - valor < self._limite_conta():
            print(f'Você não tem saldo suficiente')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite(self):
        print(f'Seu limite de cheque especial é de: R${self._limite_conta()}')

    def consultar_transacoes(self):
        print('Histórico Transações:')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self,valor,conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))

class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br

    def __init__(self,titular,conta_corrente):
        self.numero = randint(1000000000000000,9999999999999999)
        self.titular = titular
        self.validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year+4}'
        self.cod_seguranca = f'{randint(0,9)}{randint(0,9)}{randint(0,9)}'
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self,valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova senha inválida!")

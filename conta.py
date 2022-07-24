from abc import ABC, abstractmethod
from DesafioBanco.Cliente import Cliente


class Conta(ABC, Cliente):
    def __init__(self, agencia, conta, saldo, cliente):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.clienteNome, self.clienteIdade = cliente.nome, cliente.idade
        self.nomeclasse = self.__class__.__name__

    def detalhes(self):
        print(
            f'Cliente: {self.clienteNome}, Idade: {self.clienteIdade} Anos. Agencia: {self.agencia}, Conta: {self.conta}, Saldo: {self.saldo}, Tipo de Conta: {self.nomeclasse}')

    def depositar(self, valor):
        if isinstance(valor, int) or isinstance(valor, float):
            self.saldo += valor
            self.detalhes()
        else:
            print('Coloque um valor valido')

    @abstractmethod
    def sacar(self):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, cliente, limite=100):
        super().__init__(agencia, conta, saldo, cliente)
        self.limite = limite

    def sacar(self, valor):
        if not isinstance(valor, int) or isinstance(valor, float):
            print('Digite um valor valido.')
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
        else:
            self.saldo -= valor
            self.detalhes()


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if not isinstance(valor, int) or isinstance(valor, float):
            print('Digite um valor valido.')
        if valor > self.saldo:
            print('Saldo insuficiente')
        else:
            self.saldo -= valor
            self.detalhes()

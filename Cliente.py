class Pessoa():
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        self._conta = None

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def add_conta(self, conta):
        self._conta = conta

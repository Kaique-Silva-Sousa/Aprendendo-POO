class Banco():
    def __init__(self):
        self.agencia = [1111, 2222, 3333]
        self.conta = []
        self.cliente = []

    def add_cliente(self, cliente):
        self.cliente.append(cliente)

    def add_conta(self, conta):
        self.conta.append(conta.conta)

    def check(self, cliente):
        if not cliente in self.cliente:
            return False
        if not cliente._conta.agencia in self.agencia:
            return False
        if not cliente._conta.conta in self.conta:
            return False
        else:
            return True


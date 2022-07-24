from DesafioBanco.banco import Banco
from DesafioBanco.Cliente import Cliente
from DesafioBanco.conta import ContaCorrente, ContaPoupanca

banco = Banco()
c1 = Cliente('Kaique', 17)
c1conta = ContaPoupanca(1111, 1111, 0, c1)
c1.add_conta(c1conta)
banco.add_conta(c1conta)
banco.add_cliente(c1)

c2 = Cliente('Mel', 22)
c2conta = ContaCorrente(2222, 1111, 0, c2)
c2.add_conta(c2conta)
banco.add_conta(c2conta)
banco.add_cliente(c2)

if banco.check(c1):
    print('Autenticado')
    c1._conta.depositar(90)
    # c1._conta.sacar(90)
else:
    print('Usuario Invalido.')

if banco.check(c2):
    print('Autenticado')
    c2._conta.depositar(90)
    # c2._conta.sacar(90)
else:
    print('Usuario Invalido.')

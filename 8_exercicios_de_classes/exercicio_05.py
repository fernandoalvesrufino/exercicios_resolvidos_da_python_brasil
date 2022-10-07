# Exercício 5 - Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, 
# nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os 
# demais atributos são obrigatórios.

class ContaCorrente:
  def __init__(self, numero_conta, nome_correntista, saldo = 0):
    self.numero_conta = numero_conta
    self.nome_correntista = nome_correntista
    self.saldo = saldo

  def alterar_nome(self, nome):
    self.nome = nome
    print(f'O novo nome adicionado é {self.nome}')

  def deposito(self, valor):
    self.saldo += valor
    print(f'O novo saldo é de R$ {self.saldo:.2f}')

  def saque(self, valor):
    self.saldo -= valor
    print(f'O novo saldo é de R$ {self.saldo:.2f}')


cliente = ContaCorrente(1234, 'Fernando', 500)

print(cliente.__dict__)
cliente.alterar_nome('Gabriella')
cliente.deposito(5000)
cliente.saque(1000)

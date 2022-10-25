# Exercício 14 - Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
# Exemplo de uso:
# >>> harry=funcionário("Harry",25000)
# >>> harry.aumentarSalario(10)

class Funcionario():
  def __init__(self, nome, salario):
    self.nome = nome
    self.salario = salario

  def imprimirNome(self):
    print(f'Nome do funcionário: {self.nome}')

  def imprimirSalario(self):
    print(f'O salário de {self.nome} é R$ {self.salario:.2f}')

  def aumentarSalario(self, porcentagem):
    self.salario += self.salario * (porcentagem/100)
    print(f'O novo salário de {self.nome} é R$ {self.salario:.2f}')


fernando = Funcionario('Fernando Rufino', 10000)
fernando.imprimirNome()
fernando.imprimirSalario()
fernando.aumentarSalario(10)

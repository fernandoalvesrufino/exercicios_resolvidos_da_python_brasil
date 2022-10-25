# Exercício 13 - Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor 
# com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.

class Funcionario():
  def __init__(self, nome, salario):
    self.nome = nome
    self.salario = salario

  def imprimirNome(self):
    print(f'Nome do funcionário: {self.nome}')

  def imprimirSalario(self):
    print(f'O salário de {self.nome} é R$ {self.salario:.2f}')

    
fernando = Funcionario('Fernando Rufino', 10000)
fernando.imprimirNome()
fernando.imprimirSalario()

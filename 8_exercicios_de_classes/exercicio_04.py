# Exercício 4 - Classe Pessoa: Crie uma classe que modele uma pessoa:

# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer.

# Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
  def __init__(self, nome, idade, peso, altura):
    self.nome = nome
    self.idade = idade
    self.peso = peso
    self.altura = altura

  
  def envelhecer(self, anos):
    self.idade += anos
    print(self.idade)

  def engordar(self, kilos):
    self.peso += kilos
    print(self.peso)

  def emagrecer(self, kilos):
    self.peso -= kilos
    print(self.peso)

  def crescer(self):
    if self.idade < 21:
      for i in range(self.idade + 1, 21):
        self.idade += 1
        self.altura += 0.005
    else:
      self.altura = self.altura
    print(f'A altura é igual a {self.altura:.2f} m')

programador = Pessoa('Fernando', 16, 84, 1.84)

print(programador.__dict__)
programador.crescer()
programador.envelhecer(15)
programador.engordar(10)
programador.emagrecer(2)

# Exercício 3 - Classe Retangulo: Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e 
# calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def mudar_valor_dos_lados(self, nova_base, nova_altura):
    self.base = nova_base
    self.altura = nova_altura

  def retornar_valor_dos_lados(self):
    print(f'O valor da base é {self.base} e o valor da altura é {self.altura}')

  def calcular_area(self):
    area = self.base * self.altura
    print(f'O valor da área é de {area} cm2')

  def calcular_perimetro(self):
    perimetro = 2 * (self.base + self.altura)
    print(f'O perímetro do retângulo é igual a {perimetro} cm')

r_1 = Retangulo(2, 3)

print(r_1.__dict__)
r_1.retornar_valor_dos_lados()
r_1.calcular_area()
r_1.calcular_perimetro()
print()
r_1.mudar_valor_dos_lados(5, 3)
print(r_1.__dict__)
r_1.retornar_valor_dos_lados()
r_1.calcular_area()
r_1.calcular_perimetro()

# Exercício 2 - Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
  def __init__(self, tamanho_do_lado):
    self.tamanho_do_lado = tamanho_do_lado

  def mudar_valor_do_lado(self):
    novo_valor = int(input("Informe o novo valor do lado: "))
    self.tamanho_do_lado = novo_valor

  def retornar_valor_do_lado(self):
    print(f'O novo valor do lado é {self.tamanho_do_lado}')
    
  def calcular_area(self):
    area = self.tamanho_do_lado ** 2
    print(f'A área do quadrado é {area} m2')
  

quadrado_magico = Quadrado(5)

print(f'O tamanho do lado do objeto "quadrado_magico" inicial é {quadrado_magico.tamanho_do_lado}')
quadrado_magico.mudar_valor_do_lado()
quadrado_magico.retornar_valor_do_lado()
quadrado_magico.calcular_area()

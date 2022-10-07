# Exercício 1 - Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
  def __init__(self, cor, circunferencia, material):
    self.cor = cor
    self.circunferencia = circunferencia
    self.material = material

  def troca_cor(self):
    self.cor = 'Blue'

  def mostra_cor(self):
    print(self.cor)


bola_basquete = Bola('Laranja', 20, 'Borracha')

bola_basquete.troca_cor()
bola_basquete.mostra_cor()

print(bola_basquete.material)

# Exercício 8 - Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e 
# digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando 
# o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:
  def __init__(self, nome):
    self.nome = nome
    self.bucho = []

  def comer(self, alimento):
    self.bucho.append(alimento)

  def ver_bucho(self):
    print(f'Coisas no bucho: {self.bucho}')

  def digerir(self):
    print('Digerindo...')
    self.ver_bucho()
    self.bucho = []
    print('Digerido!!! Estômago Vazio!')


zoobomafoo = Macaco('Zoobomafoo')
rei_juliart = Macaco('Rei Juliart')
zoobomafoo.comer('Maça')
zoobomafoo.comer('Pera')
zoobomafoo.ver_bucho()
rei_juliart.comer('Arroz')
rei_juliart.comer('Feijão')
rei_juliart.comer('Cenoura')
rei_juliart.comer(zoobomafoo.nome)
rei_juliart.ver_bucho()
rei_juliart.digerir()


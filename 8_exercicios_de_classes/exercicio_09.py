# Exercício 9 - Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

# - Possua uma classe chamada Ponto, com os atributos x e y.
# - Possua uma classe chamada Retangulo, com os atributos largura e altura.
# - Possua uma função para imprimir os valores da classe Ponto
# - Possua uma função para encontrar o centro de um Retângulo.
# - Você deve criar alguns objetos da classe Retangulo.
# - Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
# - A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
# - O valor do centro do objeto deve ser mostrado na tela
# - Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Retangulo:
  def __init__(self, cantoinfesq_x, cantoinfesq_y, cantosupdir_x, cantosupdir_y):
    self.cantoinfesq_x = cantoinfesq_x
    self.cantoinfesq_y = cantoinfesq_y
    self.cantosupdir_x = cantosupdir_x
    self.cantosupdir_y = cantosupdir_y

  def centro(self):
    x_centro = (self.cantoinfesq_x + self.cantosupdir_x) / 2.0
    y_centro = (self.cantoinfesq_y + self.cantosupdir_y) / 2.0
    print(f'x_centro = {x_centro}, y_centro = {y_centro}')
    return Ponto(x_centro, y_centro)


x1 = int(input("Entre a coordenada x do canto inferior esquerdo: "))
y1 = int(input("Entre a coordenada y do canto inferior esquerdo: "))
canto1 = Ponto(x1, y1)
x2 = int(input("Entre a coordenada x do canto superior direito: "))
y2 = int(input("Entre a coordenada y do canto superior direito: "))
canto2 = Ponto(x2, y2)

ret = Retangulo(canto1.x, canto1.y, canto2.x, canto2.y)
ret.centro()


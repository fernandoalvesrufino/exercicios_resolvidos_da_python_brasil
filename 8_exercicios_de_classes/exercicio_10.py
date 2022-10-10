# Exercício 10 - Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

# Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# - tipoCombustivel
# - valorLitro
# - quantidadeCombustivel

# Possua no mínimo esses métodos:
# - abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
# - abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
# - alterarValor( ) – altera o valor do litro do combustível.
# - alterarCombustivel( ) – altera o tipo do combustível.
# - alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class BombaCombustivel:
  def __init__(self, quantidade_combustivel, tipo_combustivel = None):
    self.tipo_combustivel = tipo_combustivel
    self.valor_litro = 5.3
    self.quantidade_combustivel = quantidade_combustivel
    self.combustivel = ['Alcool', 'Gasolina', 'Diesel']

  def abastecerPorValor(self, valor_abastecimento, tipo_de_combustivel):
    self.quantidade_combustivel = valor_abastecimento / 5.30
    if tipo_de_combustivel in self.combustivel:
      self.tipo_combustivel = tipo_de_combustivel
    else:
      print(f'Informe entre: "Alcool", "Gasolina" ou "Diesel"')
      
  def abastecerPorLitro(self, quantos_litros, tipo_de_combustivel):
    self.quantidade_combustivel = quantos_litros
    if tipo_de_combustivel in self.combustivel:
      self.tipo_combustivel = tipo_de_combustivel
    else:
      print(f'Informe entre: "Alcool", "Gasolina" ou "Diesel"')

  def alterarValor(self, novo_valor):
    self.quantidade_combustivel = novo_valor / 5.30

  def alterarCombustivel(self, selecionar_combustível):
    self.tipo_combustivel = selecionar_combustível

  def alterarQuantidadeCombustivel(self, alterar_quantidade):
    self.quantidade_combustivel = alterar_quantidade
  
ford_ka = BombaCombustivel(0)
ford_ka.abastecerPorLitro(10, 'Gasolina')
ford_ka

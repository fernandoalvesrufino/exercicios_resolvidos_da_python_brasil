# Exercício 11 - Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

# a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
# b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
# c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
# d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
# e. Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:

# >>> meuFusca = Carro(15); # 15 quilômetros por litro de combustível.
# >>> meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
# >>> meuFusca.andar(100); # anda 100 quilômetros.
# >>> meuFusca.obterGasolina() # Imprime o combustível que resta no tanque.

class Carro:
  def __init__(self, km_por_litro, tamanho_tanque = 40, gasolina = 0):
    self.km_por_litro = km_por_litro
    self.tamanho_tanque = tamanho_tanque
    self.gasolina = gasolina

  def adicionarGasolina(self, quantidade):
    if (self.gasolina + quantidade) >= self.tamanho_tanque:
      self.gasolina = self.tamanho_tanque
      print(f'Você não pode abastecer mais do que {self.tamanho_tanque} litros. Completado o tanque')
    else:
      self.gasolina += quantidade

  def andar(self, km):
    if self.gasolina == 0:
      print('Você precisa abastecer seu carro!')
    else:
      gasolina_necessaria = km / self.km_por_litro
      if gasolina_necessaria > self.gasolina:
        print('Combustível insuficiente. Você precisa abastecer!')
        print(f'Você só andou {self.gasolina * self.km_por_litro} km. Ainda faltam cerca de {km - (self.gasolina * self.km_por_litro)} km.')
        self.gasolina = 0
      else:
        self.gasolina -= gasolina_necessaria

  def obterGasolina(self):
    print(f'Ainda tem aproximadamente {self.gasolina:.2f} litros de gasolina no tanque.')


meu_fusca = Carro(15)
meu_fusca.adicionarGasolina(20)
meu_fusca.andar(100)
meu_fusca.obterGasolina()
  

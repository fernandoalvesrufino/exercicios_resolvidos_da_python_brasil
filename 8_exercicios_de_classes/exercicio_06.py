# Exercício 6 - Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e 
# aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class Tv:
  def __init__(self, volume, canal = 1):
    self.canal = canal
    self.volume = volume

  def selecionar_canal(self, novo_canal):
    if 1 <= novo_canal <= 300:
      self.canal = novo_canal
    else:
      print('O canal informado é inválido. Por favor, selecione um canal entre 1 e 300!')
    print(f'Canal selecionado é o {self.canal}')

  def aumentar_volume(self, novo_volume):
    valido = self.volume + novo_volume
    if 0 <= valido < 101:
      self.volume = valido
      print(f'Volume atual: {self.volume}')
    elif valido > 100:
      self.volume = 100
      print(f'O valor informado ultrapassou o volume máximo. Volume máximo {self.volume} foi selecionado')
      print(f'Volume atual: {self.volume}')

  def diminuir_volume(self, novo_volume):
    valido = self.volume - novo_volume
    if 0 <= valido < 101:
      self.volume = valido
      print(f'Volume atual: {self.volume}')
    elif valido < 0:
      self.volume = 0
      print(f'O valor informado ultrapassou o volume mínimo. Volume mínimo {self.volume} foi selecionado')
      print(f'Volume atual: {self.volume}')


sony = Tv(10)
print(sony.__dict__)


sony.selecionar_canal(15)
sony.aumentar_volume(25)
sony.diminuir_volume(15)
sony.selecionar_canal(1500)

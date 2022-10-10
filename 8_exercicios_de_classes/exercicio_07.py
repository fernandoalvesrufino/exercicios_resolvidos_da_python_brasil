# Exercício 7 - Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

# - Atributos: Nome, Fome, Saúde e Idade
# - Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade

# Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, 
# ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
  
class BichinhoVirtual:
  def __init__(self, nome, fome, saude, idade):
    self.nome = nome
    self.fome = fome
    self.saude = saude
    self.idade = idade


  def alterar_nome(self, novo_nome):
    if self.idade > 80:
      print(f'{self.nome} morreu!')
    else:
      self.nome = novo_nome


  # Quanto MENOR a fome, melhor
  def alterar_fome(self, valor_fome):
    if self.idade > 80:
      print(f'{self.nome} morreu!')
    else:
      nova_fome = self.fome + valor_fome
      if 0 <= nova_fome <= 100:
        self.fome = nova_fome
      elif nova_fome < 0:
        self.fome = 0
      else:
        self.fome = 100
    

  # Quanto MAIOR a saude, melhor
  def alterar_saude(self, valor_saude):
    if self.idade > 80:
      print(f'{self.nome} morreu!')
    else:
      nova_saude = self.saude + valor_saude
      if 0 <= nova_saude <= 100:
        self.saude = nova_saude
      elif nova_saude < 0:
        self.saude = 0
      else:
        self.saude = 100
    

  def alterar_idade(self, valor_idade):
    if self.idade > 80:
      print(f'{self.nome} morreu!')
    else:
      if valor_idade < 0:
        print('Não é possível voltar no tempo! Informe uma idade positiva!')
      else:
        nova_idade = self.idade + valor_idade
        if 0 <= nova_idade <= 80:
          self.idade = nova_idade
        elif nova_idade < 0:
          self.idade = 0
        else:
          self.idade = 81
          print(f'{self.nome} morreu!')


  def retornar_nome(self):
    if self.idade > 80:
      print(f'{self.nome} morreu!')
    else:
      return print(f'Nome: {self.nome}')


  def retornar_fome(self):
    if self.idade > 80:
      print(f'{self.nome} morreu!')
    else:
      humor = (self.saude + (100 - self.fome)) / 2
      if 0 <= humor <= 20:
        humor_str = 'Péssimo'
      elif 21 <= humor <= 44:
        humor_str = 'Mal'
      elif 45 <= humor <= 54:
        humor_str = 'Normal'
      elif 55 <= humor < 89:
        humor_str = 'Bem'
      else:
        humor_str = 'Excelente'
      print(f'Humor = {humor_str} ({humor:.1f}%)')
      return print(f'Fome: {self.fome}%')


  def retornar_saude(self):
    if self.idade > 80:
      print(f'{self.nome} morreu!')
    else:
      humor = (self.saude + (100 - self.fome)) / 2
      if 0 <= humor <= 20:
        humor_str = 'Péssimo'
      elif 21 <= humor <= 44:
        humor_str = 'Mal'
      elif 45 <= humor <= 54:
        humor_str = 'Normal'
      elif 55 <= humor < 89:
        humor_str = 'Bem'
      else:
        humor_str = 'Excelente'
      print(f'Humor = {humor_str} ({humor:.1f}%)')
      return print(f'Saúde: {self.saude}%')
    

  def retornar_idade(self):
    if self.idade > 80:
      print(f'{self.nome} morreu!')
    else:
      return print(f'Idade: {self.idade}')


humor_str = ''

tigre = BichinhoVirtual('Fetolino', 70, 50, 2)
print(tigre.__dict__)

tigre.alterar_fome(-7)
tigre.retornar_fome()
tigre.retornar_nome()
tigre.alterar_idade(-10)
tigre.alterar_idade(10)
tigre.retornar_idade()
tigre.alterar_saude(12)
tigre.retornar_saude()
print(tigre.__dict__)


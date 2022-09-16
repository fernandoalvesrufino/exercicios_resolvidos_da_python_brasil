# Exercício 12 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada.

numero = int(input('Você deseja ver a tabuada de qual número? '))

for i in range(11):
  print(f'{numero} x {i} = {numero * i}')
  

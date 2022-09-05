# Exercício 23 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal.

numero = float(input('Digite um número: '))
if numero % 1 == 0:
  print(f'O número {numero} é inteiro!')
else:
  print(f'O número {numero} é decimal!')

# Exercício 22 - Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

numero = float(input('Digite um número: '))
par_ou_impar = numero % 2

if par_ou_impar == 0:
  print(f'\nO número {numero} é par!')
else:
  print(f'\nO número {numero} é impar!')

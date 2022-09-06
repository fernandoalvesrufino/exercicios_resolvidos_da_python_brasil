# Exercício 17 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input('Informe um ano: '))

if (ano % 4) == 0:
  print(f'{ano} É um ano bissesto.')
else:
  print(f'{ano} NÃO é um ano bissesto.')
  

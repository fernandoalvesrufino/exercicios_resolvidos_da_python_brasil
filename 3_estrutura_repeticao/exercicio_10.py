# Exercício 10 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

inicio = int(input('Digite o número de início: '))
final = int(input('Digite o número final: '))

for i in range((inicio + 1), final):
  print(i, end = ' ')
  

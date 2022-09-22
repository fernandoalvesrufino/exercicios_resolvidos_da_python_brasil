# Exercício 7 - Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

import math

vetor = []
produto = 1

for i in range(1,6):
  numero = int(input(f'Digite o {i} número: '))
  vetor.append(numero)
  produto *= numero

print()
print(f'A soma dos números é igual a {sum(vetor)}.')
print(f'O produto dos números é igual a {produto}.')
print(f'Os números digitados foram: {vetor}')

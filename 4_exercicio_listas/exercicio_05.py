# Exercício 5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

vetor = []
pares = []
impares = []

for i in range(5):
  numero = int(input('Digite um número: '))
  vetor.append(numero)
  if numero % 2 == 0:
    pares.append(numero)
  else:
    impares.append(numero)

print(f'Números digitados: {vetor}')
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')

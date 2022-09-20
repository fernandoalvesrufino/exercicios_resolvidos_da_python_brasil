# Exercício 1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor = []

for _ in range(5):
  numero = int(input('Digite um número: '))
  vetor.append(numero)

print('\n')
print(vetor)

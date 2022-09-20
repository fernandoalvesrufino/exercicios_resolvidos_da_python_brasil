# Exercício 2 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = []

for i in range(10):
  numero = int(input('Digite um número: '))
  vetor.append(numero)

vetor.sort()

print('\n')
print(vetor)

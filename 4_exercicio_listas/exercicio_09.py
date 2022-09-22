# Exercício 9 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

vetor = []

for _ in range(5):
  numero = int(input('Digite um número: '))
  dobro = numero ** 2
  vetor.append(dobro)


print(f'A soma dos quadrados dos valores/elementos da lista é igual a {sum(vetor)}.')

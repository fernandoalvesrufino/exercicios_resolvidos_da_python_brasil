# Exercício 17 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input('Digite um número que você deseja calcular o fatorial: '))

for i in range((numero - 1), 1, -1):
  numero = numero * i

print(numero)

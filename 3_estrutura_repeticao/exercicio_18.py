# Exercício 18 - Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

conjunto = int(input('Quantos números tem o conjunto: '))
maior = 0
menor = 999999999
soma = 0

for i in range(conjunto):
  numero = int(input('Digite um número: '))
  if numero > maior:
    maior = numero
  if numero < menor:
    menor = numero
  soma = soma + numero


print(f'''
Maior: {maior} 
Menor: {menor}
Soma: {soma}
''')

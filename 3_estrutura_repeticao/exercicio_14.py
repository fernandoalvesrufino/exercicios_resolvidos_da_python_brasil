# Exercício 14 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

par = 0
impar = 0

for i in range(6):
  numero = int(input('Digite um número: '))
  if numero % 2 == 0:
    par += 1
  else:
    impar += 1

print(f'''
Quantidade de números pares: {par}
Quantidade de números ímpares: {impar}
''')

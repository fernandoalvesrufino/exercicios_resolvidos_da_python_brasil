# Exercício 1 - Faça um programa para imprimir:
# - 1
# - 2   2
# - 3   3   3
# - .....
# - n   n   n   n   n   n  ... n

# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def triangulo_numerico(n):
  for i in range(n + 1):
    for x in range(i):
      print(i, end = '  ')
    print()
  print()


numero = int(input('Informe um número: '))
triangulo_numerico(numero)

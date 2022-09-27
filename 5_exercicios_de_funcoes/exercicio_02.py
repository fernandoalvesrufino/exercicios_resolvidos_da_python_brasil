# Exercício 2 - Faça um programa para imprimir:

# 1
# 1   2
# 1   2   3
# .....
# 1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def triangulo_numerico(n):
  for i in range(n + 2):
    for x in range(1, i):
      print(x, end = '  ')
    print()
  print()

numero = int(input('Informe um número: '))
triangulo_numerico(numero)

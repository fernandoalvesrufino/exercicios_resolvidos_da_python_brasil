# Exercício 35 - Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro 
# informado pelo usuário.

numero = int(input('Informe o valor de N para visualizar os números primos entre 1 e N: '))

for n in range(2, numero + 1):
  cont = 0
  for i in range(1, n + 1):
    if n % i == 0:
      cont += 1
    else:
      cont = cont

  if cont == 2:
    print(n, end = ' ')


# números primos de 2 à 100:
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

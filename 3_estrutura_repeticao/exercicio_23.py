# Exercício 23 - Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

numero = int(input('Informe o valor de N para visualizar os números primos entre 1 e N: '))
div = 0
div_certas = 0

for n in range(2, numero + 1):
  cont = 0
  for i in range(1, n + 1):
    if n % i == 0:
      cont += 1
      div += 1
    else:
      cont = cont

  if cont == 2:
    print(n, end = ' ')
    div_certas += 1

print()
print(f'Foram realizadas {div} divisões para encontrar os números primos.')
print()
print(f'No intervalo de 1 até {numero} foram encontrados {div_certas} números primos.')

# números primos de 2 à 100:
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

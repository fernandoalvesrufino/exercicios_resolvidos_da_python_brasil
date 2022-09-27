# Exercício 4 - Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’,
# se seu argumento for zero ou negativo.

def positivo_ou_negativo(n):
  if n <= 0:
    print('N')
  else:
    print('P')


valor_1 = positivo_ou_negativo(213)
valor_2 = positivo_ou_negativo(-345)
valor_3 = positivo_ou_negativo(0)

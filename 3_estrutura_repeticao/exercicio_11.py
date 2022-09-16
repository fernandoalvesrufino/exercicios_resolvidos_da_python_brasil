# Exercício 11 - Altere o programa anterior para mostrar no final a soma dos números.

inicio = int(input('Digite o número de início: '))
final = int(input('Digite o número final: '))
soma = 0

for i in range((inicio + 1), final):
  soma = soma + i
  print(i, end = ' ')

print()
print(soma)

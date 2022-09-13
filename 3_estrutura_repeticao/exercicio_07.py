# Exercício 7 - Faça um programa que leia 5 números e informe o maior número.

maior = -99999

for i in range(5):
  numero = float(input('Informe um número: '))
  if numero > maior:
    maior = numero

print()
print(f'O maior número informado foi {maior}.')

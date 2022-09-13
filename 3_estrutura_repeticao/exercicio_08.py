# Exercício 8 - Faça um programa que leia 5 números e informe a soma e a média dos números.

total = 0

for i in range(5):
  numero = float(input("Digite um número: "))
  total += numero

media = total / 5

print()
print(f'A soma dos números é {total} e a média é {media}.')

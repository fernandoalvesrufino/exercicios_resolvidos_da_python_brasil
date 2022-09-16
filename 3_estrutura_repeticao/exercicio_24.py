# Exercício 24 - Faça um programa que calcule o mostre a média aritmética de N notas.

numero = int(input('Quantas notas você deseja calcular? '))
notas = []

for i in range(numero):
  nota = int(input(f'Informe a {i + 1}ª nota: '))
  notas.append(nota)

media = sum(notas) / len(notas)
print()
print(f'Média: {media:.0f}')

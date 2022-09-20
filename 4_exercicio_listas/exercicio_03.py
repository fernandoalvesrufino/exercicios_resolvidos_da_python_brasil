# Exercício 3 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

nota = []

for i in range(1,5):
  numero = float(input(f'Digite a {i}ª nota: '))
  nota.append(numero)

media = sum(nota) / len(nota)
print(f'As notas tiradas foram: {nota}.')
print(f'A média final é igual a {media}.')

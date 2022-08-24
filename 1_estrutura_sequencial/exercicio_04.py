# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

number_1 = float(input('Digite a nota do primeiro bimestre: '))
number_2 = float(input('Digite a nota do segundo bimestre: '))
number_3 = float(input('Digite a nota do terceiro bimestre: '))
number_4 = float(input('Digite a nota do quarto bimestre: '))
media = (number_1 + number_2 + number_3 + number_4) / 4

print(f'A média do aluno é {media}.')

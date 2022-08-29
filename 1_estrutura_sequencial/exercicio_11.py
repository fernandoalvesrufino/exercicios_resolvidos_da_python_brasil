# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# - o produto do dobro do primeiro com metade do segundo .
# - a soma do triplo do primeiro com o terceiro.
# - o terceiro elevado ao cubo.

number_1 = int(input('Digite um número inteiro: '))
number_2 = int(input('Digite outro número inteiro: '))
number_3 = float(input('Digite um número real: '))

produto_dobro = (number_1 * 2) * (number_2 / 2)
soma_triplo = (number_1 * 3) + number_3
cubo_terceiro = number_3 ** 3
print(f'\nO produto do dobro do primeiro com metade do segundo é {produto_dobro}.')
print(f'A soma do triplo do primeiro com o terceiro {soma_triplo}.')
print(f'O terceiro elevado ao cubo {cubo_terceiro}.')

# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
# litros, que custam R$ 80,00. Informe ao usuario a quantidade de latas de tinta a serem compradas e o preço total.

tamanho_metros = float(input('Quantos metros quadrados você irá pintar? '))
cobertura_tinta = tamanho_metros / 3        # quantidade de tinta necessária
litros = cobertura_tinta % 18               # calculo do resto para descobrir se é necessário ou não uma lata a mais
latas = cobertura_tinta // 18               # calculo do valor inteiro da divisão caso não seja necessário mais uma lata

if litros == 0:
    preco = latas * 80
else:
    latas = latas + 1
    preco = latas * 80

print(f'Você vai precisar de {latas:.0f} lata(s) de 18 L e custará R$ {preco:.2f}')

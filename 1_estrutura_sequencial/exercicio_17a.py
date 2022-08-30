'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta
é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

from math import ceil

m_2 = float(input('Quantos m2 serão pintados? '))
litros = m_2 / 6
lata = litros / 18
print(f'Você vai precisar de {litros:.2f} litros de tinta para a obra.')
if litros % 18 == 0:
    print(f'Precisará comprar {lata:.0f}x lata(s) de tinta de 18 L. Você irá gastar R${lata*80:.2f}')
else:
    resto = litros - int(lata) * 18
    if resto > 10.8:
        print(f'Precisará comprar {ceil(lata):.0f}x lata(s) de tinta de 18 L. Você irá gastar R${ceil(lata)*80:.2f}')
    else:
        z = int(lata)
        y = ceil(resto / 3.6)
        print(f'Precisará comprar {z:.0f}x lata(s) de 18 L e {y:.0f}x galão(ões) de 3,6 L. '
              f'Você irá gastar R${z * 80 + y * 25:.2f}')

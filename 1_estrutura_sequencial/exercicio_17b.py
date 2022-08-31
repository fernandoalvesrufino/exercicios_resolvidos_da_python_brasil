'''

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

- Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
os valores para cima, isto é, considere latas cheias.
'''

from math import ceil
m2 = float(input('Quantos m2 serão pintados? '))
litros = float(m2 / 6)
lata = litros / 18
print(f'\nVocê vai precisar de {litros:.2f} litros de tinta para a obra.')
if litros % 18 == 0:
    print('Precisará comprar {lata:.0f}x lata(s) de tinta de 18 L.\n\nPreço total: R${lata*80:.2f}')
elif litros % 18 > 10.8:
    # Se o resto da divisão por 18 for maior que 10.8L, compensa mais comprar mais uma lata de 18
    print(f'Precisará de {int(lata)+1:.0f}x lata(s) de tinta de 18L.\n\nPreço total: R${(int(lata)+1)*80:.2f}')
else:
    # Se o resto da divisão por 18 for menor que 10.8L
    resto = (litros - int(lata) * 18) / 3.6
    # Armazena na variável resto a quantidade de litros que sobrou, menor ou igual a 10.8L
    print(f'Precisará de {int(lata)}x lata(s) de 18L e {ceil(resto)}x galão(ões) de 3,6L.')
    print(f'\nPreço total: R${int(lata)*80+ceil(resto)*25:.2f}')

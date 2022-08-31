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

from math import ceil                                                             #ceil - arredonda valor

m_2 = float(input('Quantos m2 serão pintados? '))
litros = m_2 / 6                                                                  # Qtde de litros necessários para pintar
lata = litros / 18
print(f'Você vai precisar de {litros:.2f} litros de tinta para a obra.')          # Qtde de latas necessárias
if litros % 18 == 0:                                                              # Se o valor for exato (caso apenas as latas de 18 litros atendam a necessidade)
    print(f'Precisará comprar {lata:.0f}x lata(s) de tinta de 18 L. '
          f'Você irá gastar R${lata*80:.2f}')
else:                                                                             # Se não for exato (ainda precise de mais um pouco alem das latas de 18 litros)
    resto = litros - int(lata) * 18                                               # Armazena na variável resto a quantidade de litros que ainda é necessário
    if resto > 10.8:                                                              # E o resto for maior que 10.8 litros (acima desse quantidade compensa mais comprar outra lata de 18L)
        print(f'Precisará comprar {ceil(lata):.0f}x lata(s) de tinta de 18 L. '   # Arredonda a quantidade de latas pra cima (pois compensa mais comprar outra lata de 18L)
              f'Você irá gastar R${ceil(lata)*80:.2f}')
                                                                                  
    else:
        quantidade_latas = int(lata)                                              # Pega apenas o valor inteiro da divisão (quantidade de latas de 18L)
        quantidade_galoes = ceil(resto / 3.6)                                     # Armazena na variável quantos galoes de 3.6L serão necessários                
        print(f'Precisará comprar {quantidade_latas:.0f}x lata(s) de 18 L '
              f'e {quantidade_galoes:.0f}x galão(ões) de 3,6 L. '
              f'Gasto total = R${quantidade_latas*80 + quantidade_galoes*25:.2f}')

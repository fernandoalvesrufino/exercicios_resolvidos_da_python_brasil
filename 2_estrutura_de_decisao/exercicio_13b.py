# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

dia_numero = list(range(1, 8))
dia_extenso = ['DOMINGO', 'SEGUNDA', 'TERÇA', 'QUARTA', 'QUINTA', 'SEXTA', 'SÁBADO']
while True:
    dia = int(input('Digite um número correspondente ao dia da semana (entre 1 e 7): '))
    if 0 < dia < 8:
        posicao_dia = dia_numero.index(dia)
        print(dia_extenso[posicao_dia])
        break
    else:
        print('Valor inválido!')

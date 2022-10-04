# Exercício 6 - Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

# Data de Nascimento: 29/10/1973
# Você nasceu em 29 de Outubro de 1973.

mes_extenso = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

print('Qual a data do seu nascimento? ')
print(f'''
Ex: Dia: XX
    Mês: XX
    Ano: XXXX
''')

dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

print()
print(f'Você nasceu em {dia} de {mes_extenso[mes - 1]} de {ano}')


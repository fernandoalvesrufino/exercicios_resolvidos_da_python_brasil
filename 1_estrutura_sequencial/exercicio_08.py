'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''

ganho_por_hora = float(input('Quanto você ganha por hora? R$ '))
horas_trabalhadas = int(input('Quantas horas você trabalhou nesse mês? '))

salario = ganho_por_hora * horas_trabalhadas
print(f'Nesse mês você irá receber R${salario:.2f}')

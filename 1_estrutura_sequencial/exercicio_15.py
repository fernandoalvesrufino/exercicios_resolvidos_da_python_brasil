'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

- salário bruto.
- quanto pagou ao INSS.
- quanto pagou ao sindicato.
- o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

ganho_hora = float(input('Quanto você ganha por hora? R$ '))
horas_trabalhadas = float(input('Quantas horas você trabalhou nesse mês? '))

salario_bruto = ganho_hora * horas_trabalhadas
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
sal_liquido = salario_bruto - (imposto_renda + inss + sindicato)
print(f'\nSalário bruto = R$ {salario_bruto:.2f}')
print('\nDESCONTOS:')
print(f'Imposto de Renda = R$ {imposto_renda:.2f}')
print(f'INSS = R$ {inss:.2f}')
print(f'Sindicato = R$ {sindicato:.2f}')
print(f'\nSalário Líquido = R$ {sal_liquido:.2f}')

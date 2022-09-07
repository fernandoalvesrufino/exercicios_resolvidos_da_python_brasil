# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
# depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
# Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
# descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20%

# Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

sal_hora = float(input('Informe quanto você ganha por hora: R$ '))
horas = float(input('Informe quantas horas você trabalhou no mês: '))
sal_bruto = sal_hora * horas

if sal_bruto <= 900:
    porc = 0
    ir = sal_bruto
elif sal_bruto <= 1500:
    porc = 5
    ir = sal_bruto * 0.05
elif sal_bruto <= 2500:
    porc = 10
    ir = sal_bruto * 0.1
elif sal_bruto > 2500:
    porc = 20
    ir = sal_bruto * 0.2

inss = sal_bruto * 0.1
sindicato = sal_bruto * 0.03
fgts = sal_bruto * 0.11
tot_desc = ir + sindicato + inss
sal_liq = sal_bruto - tot_desc

print(f'\nSalário Bruto ({sal_hora} * {horas}) = R$ {sal_bruto:.2f}')
print(f'(-) IR ({porc:.0f}%) = R$ {ir:.2f}')
print(f'(-) INSS (10%) = R$ {inss:.2f}')
print(f'(-) Sindicato (3%) = R$ {sindicato:.2f}')
print(f'FGTS (11%) = R$ {fgts:.2f}')
print(f'Total de descontos = R$ {tot_desc:.2f}')
print(f'\nSalário Líquido = R$ {sal_liq:.2f}')

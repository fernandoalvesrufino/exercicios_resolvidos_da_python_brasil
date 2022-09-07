# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
# desenvolver o programa que calculará os reajustes.

# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado
# no salário atual:
# - salários até R$ 280,00 (incluindo): aumento de 20%
# - salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# - salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
# - salários de R$ 1500,00 em diante: aumento de 5%

# Após o aumento ser realizado, informe na tela:
# - o salário antes do reajuste;
# - o percentual de aumento aplicado;
# - o valor do aumento;
# - o novo salário, após o aumento.


aumento = 0
novo_salario = 0

salario = float(input('Informe o salário do colaborador: R$ '))
if salario <= 280:
    aumento = 20
    novo_salario = salario + (salario * (aumento/100))
elif (salario > 280) and (salario <= 700):
    aumento = 15
    novo_salario = salario + (salario * (aumento/100))
elif (salario > 700) and (salario <= 1500):
    aumento = 10
    novo_salario = salario + (salario * (aumento/100))
elif salario > 1500:
    aumento = 5
    novo_salario = salario + (salario * (aumento/100))

print(f'O salário anterior do colaborador era de R$ {salario:.2f}.')
print(f'Houve um aumento de {aumento}%.')
print(f'O colaborador teve um aumento de salário de R$ {(salario*(aumento/100)):.2f}.')
print(f'O novo salário do colaborador é R$ {novo_salario:.2f}')

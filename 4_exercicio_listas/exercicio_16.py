# Exercício 16 - Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe 200.00 
# por semana mais 9% de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de 3000.00 em uma semana recebe 200.00 mais 
# 9% de 3000.00, ou seja, um total de 470.00. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos 
# seguintes intervalos de valores:

# 200 - 299
# 300 - 399
# 400 - 499
# 500 - 599
# 600 - 699
# 700 - 799
# 800 - 899
# 900 - 999
# 1000 em diante
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

comissao = []
cont = 0

funcionarios = int(input('Informe a quantidade de salários que deseja verificar: '))

print()

for i in range(funcionarios):
  vendas = float(input(f'Informe o valor das vendas dessa semana do funcionário {i + 1}: R$'))
  calculo = 200 + (vendas * 0.09)
  comissao.append(calculo)
  print(f'R${calculo:.2f}')

print()

for i in range(200, 999, 100):
  for s in range(len(comissao)):
    if i <= comissao[s] < (i + 100):
      cont += 1
  print(f'R${i:.2f} - R${i + 99:.2f} -> {cont}')
  cont = 0

for _ in range(len(comissao)):
  if comissao[_] > 1000:
    cont += 1
print(f'R$1000.00 em diante -> {cont}')

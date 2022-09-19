# Exercício 38 - Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

# - Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# - Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# - A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse 
# funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

salario = float(input('Informe o salário inicial: R$ '))
porc = 1.5
salario_1 = salario + (salario * (porc / 100))
print(f'R$ {salario_1:.2f}')
tempo = 2022 - 1997
print(f'{tempo} anos')

for i in range(tempo + 1):
  porc = porc * 2
  print(1997 + i)
  print(f'{porc} %')
  salario_1 = salario_1 + (salario_1 * (porc / 100))
  print(f'R$ {salario_1:.2f}')
  print()

# Exercício 26 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:

# Álcool:
# - até 20 litros, desconto de 3% por litro
# - acima de 20 litros, desconto de 5% por litro

# Gasolina:
# - até 20 litros, desconto de 4% por litro
# - acima de 20 litros, desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é 2,50 o preço do litro do álcool é 1,90.

alcool = 1.9
gasolina = 2.5


litros = float(input('Informe a quantidade de litros vendidos: '))


while True:
  combustivel = input('Qual foi o combustível? Digite [A] para Álcool e [G] para Gasolina: ').upper()
  if (combustivel == 'A') or (combustivel == 'G'):
    break
  
  else:
    print('Informe [A] ou [G]')


if combustivel == 'A':
  if litros <= 20:
    valor = (litros * alcool) * 0.97
  else:
    valor = (litros * alcool) * 0.95
elif combustivel == 'G':
  if litros <= 20:
    valor = (litros * gasolina) * 0.96
  else:
    valor = (litros * gasolina) * 0.94

print(f'O valor total a serpago é de R$ {valor:.2f}.')

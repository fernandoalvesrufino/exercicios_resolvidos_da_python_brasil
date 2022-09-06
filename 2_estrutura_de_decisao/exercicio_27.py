# Exercício 27 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#           |         Até 5 Kg   |    Acima de 5 Kg
# Morango   |   R$ 2.50 por Kg   |   R$ 2.20 por Kg   
# Maca      |   R$ 1.80 por Kg   |   R$ 1.50 por Kg   

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

frutas = ['MACA', 'MAÇA', 'MAÇÃ', 'MACÃ', 'MORANGO']
valor = 0

while True:
  fruta = input('Informe a fruta comprada: [Morango ou Maçã]: ').upper()
  if fruta in frutas:
    break
  else:
    print('Informe uma fruta disponível!')

peso = float(input('Informe quantos quilos: '))

if fruta == 'MORANGO':
  if peso <= 5:
    valor = 2.5 * peso
  elif peso > 5:
    valor = 2.2 * peso

elif (fruta == 'MAÇÃ') or (fruta == 'MAÇA') or (fruta == 'MACA') or (fruta == 'MACÃ'):
  if peso <= 5:
    valor = 1.8 * peso
  elif peso > 5:
    valor = 1.5 * peso

if (peso > 8) or (valor > 25):
    valor = valor * 0.9

print(f'O valor total da compra foi de R$ {valor:.2f}.')

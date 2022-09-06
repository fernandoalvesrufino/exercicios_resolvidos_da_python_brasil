# Exercício 28 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

#              |         Até 5 Kg   |    Acima de 5 Kg
# File Duplo   |   R$ 4.90 por Kg   |   R$ 4.80 por Kg   
# Alcatra      |   R$ 5.90 por Kg   |   R$ 5.80 por Kg  
# Picanha      |   R$ 6.90 por Kg   |   R$ 6.80 por Kg  

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade
# de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

print('------   Hipermercado Tabajara   ------')
tipos = ['FILE', 'FILÉ', 'FILE DUPLO', 'FILÉ DUPLO', 'ALCATRA', 'PICANHA']
desconto = 0

while True:
  tipo = input('Escolha o tipo de carne: ').upper()
  if tipo in tipos:
    break
  else:
    print('Informe um dos itens da lista: [FILE DUPLO], [ALCATRA] ou [PICANHA]: ')

quantidade = float(input('Quantos quilos? '))

while True:
  cartao = input('Deseja utilizar o cartão Tabajara para realizar a compra? [S] / [N] ').upper()
  if (cartao == 'S') or (cartao == 'N'):
    break
  else:
    print('Informe [S] para SIM ou [N] para NÃO! ')

if tipo == 'ALCATRA':
  if quantidade <= 5:
    valor = quantidade * 5.9
  elif quantidade > 5:
    valor = quantidade * 5.8
elif tipo == 'PICANHA':
  if quantidade <= 5:
    valor = quantidade * 6.9
  elif quantidade > 5:
    valor = quantidade * 6.8
else:
  if quantidade <= 5:
    valor = quantidade * 4.9
  elif quantidade > 5:
    valor = quantidade * 4.8

if cartao == 'S':
  desconto = 5
  preco_final = valor * 0.95
  valor_desconto = valor * 0.05
  tipo_pgto = 'Cartão Tabajara'.upper()
  
else:
  tipo_pgto = input('Qual a forma de pagamento? [DINHEIRO], [CRÉDITO] ou [DÉBITO]: ').upper()
  preco_final = valor
  valor_desconto = 0


print(f'''
Carne comprada: {tipo}
Quantidade: {quantidade:.2f} Kg



Preço total: R$ {valor:.2f}    

Tipo de pagmento: {tipo_pgto}
Desconto: {desconto} %
valor do desconto: R$ {valor_desconto:.2f}

Valor a pagar: R$ {preco_final:.2f}
      ''')

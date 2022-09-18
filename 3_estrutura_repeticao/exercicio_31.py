# Exercício 31 - O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
# Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
# Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o
# cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. 
# A saída deve ser conforme o exemplo abaixo:

while True:
  print('Lojas Tabajara')
  total = 0
  produto = 0
  while True:
    produto += 1
    preco = float(input(f'Produto {produto}: R$ '))
    if preco == 0:
      break
    total = total + preco

  print()
  print(f'Total: R$ {total:.2f}')
  dinheiro = float(input('Dinheiro: R$ '))
  troco = dinheiro - total
  print(f'Troco: R$ {troco:.2f}')
  print()

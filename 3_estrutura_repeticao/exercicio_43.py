# Exercício 43 - O cardápio de uma lanchonete é o seguinte:

# Especificação ---- Código ---- Preço
# Cachorro Quente --- 100 ------- 1,20
# Bauru Simples ----- 101 ------- 1,30
# Bauru com ovo ----- 102 ------- 1,50
# Hambúrguer -------- 103 ------- 1,20
# Cheeseburguer ----- 104 ------- 1,30
# Refrigerante ------ 105 ------- 1,00

# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total
# geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

pedido = []
quantidades = []
lanche = []
lista = ['Cachorro Quente', 'Bauru Simples', 'Bauru com Ovo', 'Hamburger', 'Cheeseburger', 'Refrigerante']
precos = [1.2, 1.3, 1.5, 1.2, 1.3, 1.0]
totais = []
contador = 0
quant = 0


while True:
  pedido = int(input('Informe o código do lanche que você deseja comprar: '))

  if 100 <= pedido <= 105: 

    for i in range(100,106):
      if pedido == 100 + (i - 100):
        lanche.append(lista[i - 100])
        quant = int(input('Quantidade: '))
        quantidades.append(quant)
        valor = precos[i-100] * quant
        totais.append(valor)
        contador += 1

  elif pedido == 0:
    break

  else:
    print('Informe um valor válido conforme a tabela de preços, ou digite 0 para encerrar!')
    print()

print()

for _ in range(contador):
  print(f'{quantidades[_]}x {lanche[_]} = R$ {totais[_]:.2f}')

print(f'''

Total: R$ {sum(totais):.2f}

''')

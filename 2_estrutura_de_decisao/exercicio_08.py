# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

product_1 = float(input('Digite o valor do primeiro produto: R$ '))

for i in range(2):
    price = float(input('Digite o valor de outro produto: R$ '))
    if price < product_1:
        product_1 = price
print(f'O produto mais barato custa R$ {product_1:.2f}.')

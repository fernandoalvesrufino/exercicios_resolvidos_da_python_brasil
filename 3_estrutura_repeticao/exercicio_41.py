# Exercício 41 - Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, 
# quantidade de parcelas e valor da parcela.

divida_inicial = 1000 #float(input('Informe o valor da dívida: R$ '))
parcelas = 1
valor_juros = 0
porcentagem = 0
valor_parcela = valor_juros + divida
cifrao = 'R$'
divida = divida_inicial

print('Valor da Dívida     Valor dos Juros     Quantidade de Parcelas    Valor da Parcela')
print(f' {cifrao:2} {divida:.2f} {valor_juros:16.2f} {parcelas:23.0f} {valor_parcela:25.2f}')

porcentagem = 5

for i in range(3, 13, 3):
  parcelas = i * 1
  porcentagem += 5
  valor_juros = divida_inicial * (porcentagem / 100)
  divida = divida_inicial + valor_juros
  valor_parcela = divida / parcelas


  print(f' {cifrao:2} {divida:.2f} {valor_juros:16.2f} {parcelas:23.0f} {valor_parcela:25.2f}')

# Exercício 7 - Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, 
# que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. 
# Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. 
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
# O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de 
# multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(valor_prestacao, dias_atraso):

  if dias_atraso == 0:
    valor_a_pagar = valor_prestacao
  else:
    juros = 0.01 * dias_atraso
    valor_a_pagar = valor_prestacao + (valor_prestacao * (0.03 + juros)) 
    return valor_a_pagar

total_prestacao = []

while True:
  valor = float(input('Valor da prestação: R$ '))
  if valor == 0:
    break
  else:
    dias = int(input('Dias em atraso: '))

    valor_final = valorPagamento(valor, dias)
    print(f'Valor a final - R$ {valor_final:.2f}')
    print()
    total_prestacao.append(valor_final)

print(f'''
RELATÓRIO FINAL:

Quantidades de prestações pagas: {len(total_prestacao)}
Valor total das prestações: R$ {sum(total_prestacao):.2f}

''')

# Exercício 24 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

# - par ou ímpar;
# - positivo ou negativo;
# - inteiro ou decimal.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

operacao = input('Qual operação você deseja realizar? [Somar (+), Subtrair (-), Dividir (/), Multiplicar (*)] ').upper()

if (operacao == 'SOMAR') or (operacao == '+'):
  resultado = n1 + n2
elif (operacao == 'SUBTRAIR') or (operacao == '-'):
  resultado = n1 - n2
elif (operacao == 'DIVIDIR') or (operacao == '/'):
  resultado = n1 / n2
elif (operacao == 'MULTIPLICAR') or (operacao == '*'):
  resultado = n1 * n2
else:
  print('Não foi informada uma operação válida!')

if resultado % 2 == 0:
  par_impar = 'PAR'
else:
  par_impar = 'ÍMPAR'

if resultado > 0:
  positivo_negativo = 'POSITIVO'
elif resultado < 0:
  positivo_negativo = 'NEGATIVO'
else:
  positivo_negativo = "NEUTRO"
 
if resultado % 1 == 0:
  inteiro_decimal = 'INTEIRO'
else:
  inteiro_decimal = 'DECIMAL'


print(f'\nResultado: {resultado}')
print(f'Par ou Ímpar: {par_impar}')
print(f'Positivo ou Negativo: {positivo_negativo}')
print(f'Inteiro ou Decimal: {inteiro_decimal}')

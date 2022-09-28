# Exercício 6 - Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. 
# como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. 
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def horario(hora, minuto):
  if 12 < hora <= 24 and 0 <= minuto < 60:
    hr = hora - 12
    nome = 'P.M.'
  elif 0 < hora <= 12 and 0 <= minuto < 60:
    hr = hora
    nome = 'A.M.'
  else:
    print('Valor inválido!')

  return f'{hr}:{minuto} {nome}'


while True:
  h = int(input('Horas: '))
  m = int(input('Minutos: '))
  conversao_de_hora = horario(h, m)
  print(conversao_de_hora)
  cont = input('Continuar? [S] / [N] ').upper()
  if cont == 'N':
    break

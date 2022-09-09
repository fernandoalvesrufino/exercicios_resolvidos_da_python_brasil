# Exercício 1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue 
# pedindo até que o usuário informe um valor válido.

while True:
  nota = float(input('Digite uma nota entre 0 e 10: '))
  if 0 <= nota <= 10:
    print(f'A nota digitada foi {nota:.2f}')
    break
  else:
    print('Valor INVÁLIDO. Digite uma nota entre 0 e 10!')

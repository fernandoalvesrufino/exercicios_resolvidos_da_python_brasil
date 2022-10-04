# Exercício 10 - Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

dezena = ['VINTE', 'TRINTE', 'QUARENTA', 'CINQUENTA', 'SESSENTA', 'SETENTA', 'OITENTA', 'NOVENTA']
unidade = ['UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE']
dez_a_vinte = ['DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE']

def extenso(number):
  quant_dezena = numero // 10
  quant_unidade = numero % 10

  if quant_dezena != 0:
    if quant_dezena != 1:
      if quant_unidade != 0:
        print(f'{dezena[quant_dezena - 2]} E {unidade[quant_unidade - 1]}')
      else:
        print(f'{dezena[quant_dezena - 2]}')
    else:
      print(f'{dez_a_vinte[quant_unidade]}')
  else:
    print(f'{unidade[quant_unidade - 1]}')


while True:
  try: 
    numero = int(input('Digite um número entre 0 e 99: '))
  except ValueError:
    print('Digite um número entre 0 e 99!')
    print()
  else:
    if 0 <= numero < 100:
      print(f'O número digitado foi {numero}')
      break
    else:
      print('Digite um número entre 0 e 99!')
      print()

extenso(numero)

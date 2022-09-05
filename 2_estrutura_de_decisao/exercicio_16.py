'''
Exercício 16 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

print('EQUAÇÃO DE SEGUNDO GRAU')

while True:
  a = float(input('Informe o valor de a: '))

  if a == 0:
    print('Não é uma equação de segundo grau!')
    break
  
  b = float(input('Informe o valor de b: '))
  c = float(input('Informe o valor de c: '))

  delta = (b ** 2) - (4 * a * c)
  
  if delta < 0:
    print('Para delta negativo, a equação não possui raizes reais.')
    break
  elif delta == 0:
    x1 = ((- b) + (delta ** (0.5))) / (2 * a)
    x2 = ((- b) - (delta ** (0.5))) / (2 * a)
    print(f'A equação possui apenas uma raiz real. X = {x1}.')
    break

  
  x1 = ((- b) + (delta ** (0.5))) / (2 * a)
  x2 = ((- b) - (delta ** (0.5))) / (2 * a)

  print(f'''
Valor de delta = {delta}
x = {x1} 
x" = {x2}
  ''')

  break
  

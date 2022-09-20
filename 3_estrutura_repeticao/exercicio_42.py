# Exercício 42 - Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: 
# [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

classe_1 = 0          # 0 - 25
classe_2 = 0          # 26 - 50
classe_3 = 0          # 51 - 75 
classe_4 = 0          # 76 - 100

while True:
  numero = int(input('Informe um número: '))
  if 0 <= numero <= 25:
    classe_1 += 1 
  elif 26 <= numero <= 50:
    classe_2 += 1 
  elif 51 <= numero <= 75:
    classe_3 += 1 
  elif 76 <= numero <= 100:
    classe_4 += 1 
  elif numero < 0:
    break
  else:
    print('Informe um número entre 0 e 100. Caso deseje encerrar o programa, digite um valor negativo!')

print(f'''

Quantidade de números de:
0 - 25: {classe_1}
26 - 50: {classe_2}
51 - 75: {classe_3}
76 - 100: {classe_4}

FIM DO PROGRAMA
''')

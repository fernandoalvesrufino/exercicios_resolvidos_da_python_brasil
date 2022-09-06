# Exercício 21 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e 
# depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# - Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# - Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

contador = 0
notas = []
singular_plural = []

while True:
  try:
    valor = float(input('Informe o valor que você deseja sacar: R$ '))
  except ValueError:
    print('Você deve informar um valor de no mínimo R$ 10,00 e no máximo R$ 600,00! ')
  else:
    if 10 <= valor <= 600:
      #notas disponíveis: 100, 50, 10, 5, 1
      notas_cem = valor // 100
      notas.append(notas_cem)
      notas_cinquenta = (valor % 100) // 50
      notas.append(notas_cinquenta)
      notas_dez = (valor % 50) // 10
      notas.append(notas_dez)
      notas_cinco = (valor % 10) // 5
      notas.append(notas_cinco)
      notas_um = (valor % 5) // 1
      notas.append(notas_um)

      for i in range(5):
        if notas[i] == 0:
          singular_plural.append('')
        elif notas [i] == 1:
          singular_plural.append(' nota')
        else:
          singular_plural.append(' notas')
      
      if notas_cem != 0:
        contador += 1
      if notas_cinquenta != 0:
        contador += 1
      if notas_dez != 0:
        contador += 1
      if notas_cinco != 0:
        contador += 1
      if notas_um != 0:
        contador += 1

      break
    
    else:
      print('Você deve informar um valor de no mínimo R$ 10,00 e no máximo R$ 600,00! ')

print(f'''
Para sacar a quantia de {valor} reais, você receberá:
{notas[0]:.0f} {singular_plural[0]} de 100, 
{notas[1]:.0f} {singular_plural[1]} de 50,
{notas[2]:.0f} {singular_plural[1]} de 10,
{notas[3]:.0f} {singular_plural[3]} de 5 e
{notas[4]:.0f} {singular_plural[4]} de 1
''')

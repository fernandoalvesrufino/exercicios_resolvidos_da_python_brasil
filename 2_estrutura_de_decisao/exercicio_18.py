# Exercício 18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

meses_31 = [1, 3, 5, 7, 8, 10,12]
meses_30 = [4, 6, 9, 11]

dia_valido = False
mes_valido = False
ano_valido = False

dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))

if -9999 < ano < 9999:
  ano_valido = True

if 0 < mes < 13:
  mes_valido = True 

if mes != 2:
  if mes in meses_31:
    if 0 < dia < 32:
      dia_valido = True    
  elif mes in meses_30:
    if 0 < dia < 31:
      dia_valido = True    
elif mes == 2:
  if (ano % 4) == 0:
    if 0 < dia < 30:
      dia_valido = True
  elif (ano % 4) != 0:
    if 0 < dia < 29:
      dia_valido = True
  
if (ano_valido == True) and (mes_valido == True) and (dia_valido == True):
  print()
  print('Data válida.')
else:
  print()
  print('DATA INVÁLIDA!')
  

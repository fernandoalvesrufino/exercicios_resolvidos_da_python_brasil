# Exercício 18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

meses_31 = [1, 3, 5, 7, 8, 10,12]
meses_30 = [4, 6, 9, 11]
data = []

while True: 
  ano = int(input('Informe o ano: '))
  if -9999 < ano < 9999:
    data.append(ano)
    break
  else:
    print('Informe um ano entre -9999 e 9999.')

while True:
  mes = int(input('Informe o mês: '))
  if 0 < mes < 13:
    data.append(mes)
    break
  else:
    print('Informe um mês entre 1 e 12.')

while True:
  dia = int(input('Informe o dia: '))
  if mes == 2:
    if (ano % 4) == 0:
      if 0 < dia < 30:
        data.append(dia)
        break
      else:
        print('Informe um dia entre 1 e 29.')
    elif (ano % 4) != 0:
      if 0 < dia < 29:
        data.append(dia)
        break
      else:
        print('Informe um dia entre 1 e 28.')

  
  elif mes != 2:
    if mes in meses_31:
      if 0 < dia < 32:
        data.append(dia)
        break    
      else:
        print('O mês informado possui 31 dias. Informe um dia entre 1 e 31.')
    elif mes in meses_30:
      if 0 < dia < 31:
        data.append(dia)
        break
      else:
        print('O mês informado possui 30 dias. Informe um dia entre 1 e 30.')  

data_ajustada = [data[2], data[1], data [0]]
print('/'.join(map(str, data_ajustada)))

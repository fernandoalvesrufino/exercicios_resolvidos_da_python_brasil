# Exercício 9 - Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número
# válido ou inválido através da validação dos dígitos verificadores dos caracteres de formatação.

print('---------- Verificação de CPF ----------')
print(f'''
Informe seu CPF: 
Ex: xxx.xxx.xxx-xx
OBS: Digite apenas números! Não inclua pontos nem traços
''')
while True:
  try:
    cpf = int(input('CPF: '))
  except ValueError:
    print('OBS I: Digite apenas números! Não inclua pontos nem traços!')
  else:
    caracteres = str(cpf)
    if len(caracteres) == 11:
      print('Seu CPF é: ', end = '')
      for i in range(3):
        print(caracteres[i], end = '')
      print('.', end = '')
      for i in range(3, 6):
        print(caracteres[i], end = '')
      print('.', end = '')
      for i in range(6, 9):
        print(caracteres[i], end = '')
      print('-', end = '')
      for i in range(9, 11):
        print(caracteres[i], end = '')
      break
    else:
      print('OBS II: O número de CPF deve conter 11 dígitos!')




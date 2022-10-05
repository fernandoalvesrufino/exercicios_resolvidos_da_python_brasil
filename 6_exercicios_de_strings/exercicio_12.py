# Exercício 12 - Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, 
# acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

while True:
  telefone = input('Digite um número de telefone: Ex: xxxx-xxxx: ')

  if len(telefone) == 8:
    if '-' in telefone:
      print(telefone)
    else:
      for i in range(4):
        print(telefone[i], end = '')
      print('-', end = '')
      for i in range(4,8):
        print(telefone[i], end = '')
      break

  elif len(telefone) == 7:
    if '-' in telefone:
      print(telefone)
    else:
      print('3', end = '')
      for i in range(3):
        print(telefone[i], end = '')
      print('-', end = '')
      for i in range(3,7):
        print(telefone[i], end = '')
      break

  else:
    print('Informe um número de telefone válido!')
    print()

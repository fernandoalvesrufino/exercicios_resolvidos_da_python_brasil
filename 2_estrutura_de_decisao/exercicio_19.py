# Exercício 19 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo. 

# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# - 326 = 3 centenas, 2 dezenas e 6 unidades
# - 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

contador = 0
centena = 0
dezena = 0
unidade = 0

while True:
  try:
    numero = int(input('Digite um número: '))
  except ValueError:
    print('Informe um valor entre 0 e 1000!')
  else:
    if 0 < numero < 1000:
      centena = numero // 100
      dezena = (numero % 100) // 10
      unidade = numero % 10

      if centena == 0:
        pass
      elif centena == 1:
        nome_centena = 'centena'
        contador += 1
      else:
        nome_centena = 'centenas'
        contador += 1

      if dezena == 0:
        pass
      elif dezena == 1:
        nome_dezena = 'dezena'
        contador += 1
      else:
        nome_dezena = 'dezenas'
        contador += 1

      if unidade == 0:
        pass
      elif unidade == 1:
        nome_unidade = 'unidade'
        contador += 1
      else:
        nome_unidade = 'unidades'
        contador += 1
      break
    
    else:
      print('Informe um valor entre 0 e 1000!')

if contador == 1:
  if centena != 0:
    print(f'{centena} {nome_centena}')
  elif dezena != 0:
    print(f'{dezena} {nome_dezena}')
  elif unidade != 0:
    print(f'{unidade} {nome_unidade}')
elif contador == 3:
  print(f'{centena} {nome_centena}, {dezena} {nome_dezena} e {unidade} {nome_unidade}')
elif contador == 2:
  if centena == 0:
    print(f'{dezena} {nome_dezena} e {unidade} {nome_unidade}')
  elif dezena == 0:
    print(f'{centena} {nome_centena} e {unidade} {nome_unidade}')
  elif unidade == 0:
    print(f'{centena} {nome_centena} e {dezena} {nome_dezena}')
else:
  pass

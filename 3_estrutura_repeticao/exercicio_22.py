# Exercício 22 - Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

numero = int(input('Informe um número para verificar se ele é ou não primo: '))
cont = 0
print(f'{numero} é divisível por:', end = ' ')

for i in range(1, numero + 1):
  if numero % i == 0:
    cont += 1
    print(i, end = ' ')
  else:
    cont = cont


if cont == 2:
  print('É primo.')
else:
  print()
  print(f'Não é primo, pois é divisível por {cont} números.')

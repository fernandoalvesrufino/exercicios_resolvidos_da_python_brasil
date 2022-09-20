# Exercício 50 - Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

quantidade = int(input('Quantos termos deseja verificar? '))
print('H = ', end = '')
soma = 0

for i in range(quantidade):
  if i == (quantidade - 1):
    print(f'{1}/{(i + 1)}', end = '')
    soma = soma + ((1)/(i + 1))
  else:
    print(f'{1}/{(i + 1)}', end = ' + ')
    soma = soma + ((1)/(i + 1))


print()
print(f'A soma total é: {soma:.2f}')

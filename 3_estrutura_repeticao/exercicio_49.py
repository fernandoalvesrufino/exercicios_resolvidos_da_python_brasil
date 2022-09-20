# Exercício 49 - Faça um programa que mostre os n termos da Série a seguir:

# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

# Imprima no final a soma da série.

quantidade = int(input('Quantos termos deseja verificar? '))
print('S = ', end = '')
soma = 0

for i in range(quantidade):
  if i == (quantidade - 1):
    print(f'{i + 1}/{(i * 2) + 1}', end = '')
    soma = soma + ((i + 1)/((i * 2) + 1))
  else:
    print(f'{i + 1}/{(i * 2) + 1}', end = ' + ')
    soma = soma + ((i + 1)/((i * 2) + 1))


print()
print(f'A soma total é: {soma:.2f}')

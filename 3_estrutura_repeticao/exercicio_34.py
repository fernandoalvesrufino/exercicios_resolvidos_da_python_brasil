# Exercício 34 - Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
# Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

numero = int(input('Informe um número para verificar se ele é ou não primo: '))
cont = 0

for i in range(1, numero + 1):
  if numero % i == 0:
    cont += 1
  else:
    cont = cont

if cont == 2:
  print('É primo.')
else:
  print('Não é primo.')

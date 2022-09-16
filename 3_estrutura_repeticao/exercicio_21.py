# Exercício 21 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

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

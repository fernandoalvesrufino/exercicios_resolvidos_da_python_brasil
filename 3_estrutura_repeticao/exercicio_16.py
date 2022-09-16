# Exercício 16 - A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

penultimo = 0
anterior = 1
proximo = 0

print(penultimo, anterior, end = ' ')

while proximo < 500:
  proximo = anterior + penultimo
  print(proximo, end = ' ')
  penultimo = anterior
  anterior = proximo

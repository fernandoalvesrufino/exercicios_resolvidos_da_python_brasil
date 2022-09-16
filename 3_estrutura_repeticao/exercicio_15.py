# Exercício 15 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

penultimo = 0
anterior = 1

termo = int(input('Informe quantos valores da sequência de Fibonacci você deseja visualizar: '))

print(penultimo, anterior, end = ' ')

for i in range(termo - 2):
  proximo = anterior + penultimo
  print(proximo, end = ' ')
  penultimo = anterior
  anterior = proximo

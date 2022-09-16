# Exercício 19 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

conjunto = int(input('Quantos números tem o conjunto: '))
maior = 0
menor = 1001
soma = 0

for i in range(conjunto):
  while True:
    numero = int(input('Digite um número: '))
    if 0 <= numero <= 1000:
      break
    else:
      print('Digite um número entre 0 e 100!')
  if numero > maior:
    maior = numero
  if numero < menor:
    menor = numero
  soma = soma + numero


print(f'''
Maior: {maior} 
Menor: {menor}
Soma: {soma}
''')

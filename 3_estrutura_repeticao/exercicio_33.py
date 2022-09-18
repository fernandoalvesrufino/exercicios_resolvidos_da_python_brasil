# Exercício 33 - O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado de temperaturas, 
# e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

total = 0
contador = 0
maior = 0
menor = 999999

while True:
  temperatura = float(input('Informe a temperatura: '))
  total = total + temperatura
  contador += 1
  if temperatura > maior:
    maior = temperatura
  if temperatura < menor:
    menor = temperatura
  
  continuar = input('Deseja continuar? [S] / [N] ').upper()
  if (continuar == 'N') or (continuar == 'NAO'):
    break

media = total / contador
print(f'''

Maior temperatura: {maior:.1f} ºC
Menor temperatura: {menor:.1f} ºC
Temperatura média: {media:.1f} ºC
''')

# Exercício 25 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# - "Telefonou para a vítima?"
# - "Esteve no local do crime?"
# - "Mora perto da vítima?"
# - "Devia para a vítima?"
# - "Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser 
# classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

lista = []
contador = 0

p1 = input('Telefonou para a vítima?').upper()
p2 = input('Esteve no local do crime? ').upper()
p3 = input('Mora perto da vítima? ').upper()
p4 = input('Devia para a vítima? ').upper()
p5 = input('Já trabalhou com a vítima? ').upper()

lista.append(p1)
lista.append(p2)
lista.append(p3)
lista.append(p4)
lista.append(p5)

for i in range(len(lista)):
  if (lista[i] == 'SIM') or (lista[i] == 'S'):
    contador += 1

print()

if contador == 2:
  print('Suspeita')
elif 3 <= contador <= 4:
  print('Cúmplice')
elif contador == 5:
  print('Assassino')
else:
  print('Inocente')
 

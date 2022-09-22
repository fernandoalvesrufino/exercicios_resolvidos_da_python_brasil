# Exercício 14 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada 
# como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

csi = []
respostas = 0

telefonou = input('Telefonou para a vítima? [S / N] ').upper()
csi.append(telefonou)
local = input('Esteve no local do crime? [S / N] ').upper()
csi.append(local)
mora = input('Mora perto da vítima? [S / N] ').upper()
csi.append(mora)
devia = input('Devia para a vítima? [S / N] ').upper()
csi.append(devia)
trabalhou = input('Já trabalhou com a vítima? [S / N] ').upper()
csi.append(trabalhou)

quantidade = len(csi)
for i in range(quantidade):
  if csi[i] == 'S':
    respostas += 1

print()

if respostas == 2:
  print('SUSPEITO')
elif 2 < respostas < 5:
  print('CUMPLICE')
elif respostas == 5:
  print('ASSASSINO')
else:
  print('INOCENTE')

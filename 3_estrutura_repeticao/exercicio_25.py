# Exercício 25 - Faça um programa que peça para N pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre
# 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

quantidade = int(input('Informe a quantidade de idades a serem verificadas: '))
jovem = 0
adulta = 0
idosa = 0

for i in range(quantidade):
  idade = int(input('informe a idade: '))
  if 0 <= idade <= 25:
    jovem += 1
  elif 26 <= idade <= 60:
    adulta += 1
  elif idade > 60:
    idosa += 1

print(f'''
Jovens: {jovem}
Adultos: {adulta}
Idosos: {idosa}
''')

if (jovem > adulta) and (jovem > idosa):
  print('A turma é jovem.')
elif (adulta > jovem) and (adulta > idosa):
  print('A turma é adulta.')
elif (idosa > jovem) and (idosa > adulta):
    print('A turma é idosa.')
else:
  print('A turma é neutra.') 

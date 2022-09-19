# Exercício 39 - Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em 
# centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

aluno_alto = 0
aluno_baixo = 999999
numero_alto = 0
numero_baixo = 0

for i in range(5):
  numero = int(input('Informe o número do aluno: '))
  altura = int(input('Informe a altura do aluno em centimetros: '))

  if altura > aluno_alto:
    aluno_alto = altura
    numero_alto = numero
  if altura < aluno_baixo:
    aluno_baixo = altura
    numero_baixo = numero


print(f'''
Aluno mais alto: {aluno_alto} - Número do aluno: {numero_alto}
Aluno mais baixo: {aluno_baixo} - Número do aluno: {numero_baixo}
''')

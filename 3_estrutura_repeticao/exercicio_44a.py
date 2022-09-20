# Exercício 44 - Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

# 1 , 2, 3, 4 - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:

# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

lista = ['José', 'João', 'Antônio', 'Francisco', 'Nulo', 'Votos em Branco']
cont_1 = 0
cont_2 = 0
cont_3 = 0
cont_4 = 0
cont_5 = 0
cont_6 = 0

while True:
  voto = int(input('Qual o seu voto: '))
  if 1 <= voto <= 6:
    if voto == 1:
      cont_1 += 1
    elif voto == 2:
      cont_2 += 1
    elif voto == 3:
      cont_3 += 1
    elif voto == 4:
      cont_4 += 1
    elif voto == 5:
      cont_5 += 1
    elif voto == 6:
      cont_6 += 1

  elif voto == 0:
    break

  else:
    print('Informe um número de 1 a 6. Ou digite 0 para encerrar!')

print(f'''

Votos:
{lista[0]}: {cont_1} votos
{lista[1]}: {cont_2} votos
{lista[2]}: {cont_3} votos
{lista[3]}: {cont_4} votos
{lista[4]}: {cont_5} votos
{lista[5]}: {cont_6} votos
''')




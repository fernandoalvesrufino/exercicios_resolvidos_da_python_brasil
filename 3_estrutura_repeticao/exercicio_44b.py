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
contagem = []

while True:
  voto = int(input('Qual o seu voto: '))
  if 1 <= voto <= 6:
    contagem.append(voto)
  elif voto == 0:
    break
  else:
    print('Informe um número de 1 a 6. Ou digite 0 para encerrar!')

print('\nVotos:')

for i in range(6):
  print(f'{lista[i]}: {contagem.count(i + 1)} votos')
 

# Exercício 26 - Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o 
# número de votos de cada candidato.

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0

print('Escolha um candidado.')
print()
eleitores = int(input('Informe a quantidade de eleitores: '))

for i in range(eleitores):
  voto = int(input('Informe o número do candidato: [1], [2] ou [3]: '))
  if voto == 1:
    candidato_1 += 1
  elif voto == 2:
    candidato_2 += 1
  elif voto == 3:
    candidato_3 += 1
  else:
    print('Informe um canditado válido! 1, 2 ou 3. Ou digite -1 para encerrar!')

print(f'''
Candidato 1: {candidato_1} votos
Candidato 2: {candidato_2} votos
Candidato 3: {candidato_3} votos
''')


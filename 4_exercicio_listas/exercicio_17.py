# Exercício 17 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos
# cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe 
# o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta.

atleta = []
media_salto = []
nome = 'Start'
contagem = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
salto = []
saltos_dos_atletas = []


while True:
  nome = input('Atleta: ')
  print()
  if nome == '':
    break
  else:
    atleta.append(nome)
    media = 0
    salto_do_atleta = 0

    for i in range(5):
      
      distancia_salto = float(input(f'{contagem[i]} salto: '))
      salto.append(distancia_salto)
      salto_do_atleta += distancia_salto
    media = salto_do_atleta / 5 
    media_salto.append(media)

  print()

# valores_saltos = ' - '.join(map(str, salto))

inicio = 0
fim = 5

for i in range(len(atleta)):
  print('Resultado final:')
  print(f'Atleta: {atleta[i]}')
  saltos_dos_atletas.clear()
  #for i1 in range(len(salto))
  
  for _ in range(inicio, fim):
    saltos_dos_atletas.append(salto[_])

  inicio += 5
  fim += 5
  valores_saltos = ' - '.join(map(str, saltos_dos_atletas))
  print(f'Saltos: {valores_saltos}')
  print(f'Média dos saltos: {media_salto[i]} m')
  print()

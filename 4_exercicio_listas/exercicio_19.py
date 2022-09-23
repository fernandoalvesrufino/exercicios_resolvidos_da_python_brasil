# Exercício 19 - Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações: 
# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro

# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os 
# valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
# Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular 
# a percentual de cada um dos concorrentes e informar o vencedor da enquete.

vetor = []
maior = 0

sistema_operacional = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro' ]

print('Enquete: Qual o melhor Sistema Operacional para uso em servidores? ')
print('''
1 - Windows Server
2 - Unix
3 - Linux
4 - Netware
5 - Mac OS
6 - Outro
''')

while True:
  try:
    nota = int(input('Informe qual o melhor Sistema Operacional para uso em servidores, na sua opinião: '))
  except ValueError:
    print('Você deve escolher uma opção entre 1 e 6'.upper())
  else:
    if nota == 0:
      break
    elif 0 < nota < 7:
      vetor.append(nota-1)
    else:
      print('Você deve escolher uma opção entre 1 e 6'.upper())

print()
print('Sistema Operacional     Votos     %')
print('-------------------     -----    ---')
for i in range(6):
  contador = 0
  for _ in range(len(vetor)):
    if i == vetor[_]:
      contador += 1
  porcentagem = (contador / len(vetor)) * 100
  print(f'{sistema_operacional[i]:14}{contador:13}{porcentagem:9.1f}')

  if contador > maior:
    maior = contador
    maior_porcentagem = porcentagem
    melhor_sistema = sistema_operacional[i]

print()
print('-------------------     -----    ---')
print(f'Total            {len(vetor):10}')

print(f'O Sistema Operacional mais votado foi o {melhor_sistema}, com {maior} votos, correspondendo a {maior_porcentagem:.1f}% dos votos.')

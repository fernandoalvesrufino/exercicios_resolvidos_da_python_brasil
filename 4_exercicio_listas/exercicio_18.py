# Exercício 18 - Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. 
# Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi 
# contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, 
# entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido 
# for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa 
# deverá exibir:

# O total de votos computados;

# Os númeos e respectivos votos de todos os jogadores que receberam votos;
# O percentual de votos de cada um destes jogadores;
# O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.

print('Enquete: Quem foi o melhor jogador?')
melhores_jogadores = []
maior_voto = 0
melhor_jogador = 0
melhor_porcentagem = 0

while True:
  try:
    jogador = float(input('Número do jogador: '))
  except ValueError:
    print('Informe um valor entre 1 e 23 ou 0 para sair!')
  else:
    if 0 < jogador < 24:
      melhores_jogadores.append(jogador)
    elif jogador == 0:
      break
    else:
      print('Informe um valor entre 1 e 23 ou 0 para sair!')

print()
print('Resultado da votação: ')
print()
print(f'Foram computados {len(melhores_jogadores)} votos.')
print()
print('Jogador          Votos          %')
melhores_jogadores.sort()

for i in range(24):
  contador = 0
  for _ in range(len(melhores_jogadores)):
    if i == melhores_jogadores[_]:
      contador += 1
  
  porcentagem = (contador / len(melhores_jogadores)) * 100

  if contador > maior_voto:
    melhor_jogador = i
    melhor_porcentagem = porcentagem
    maior_voto = contador
  
  if contador != 0:  
    print(f'{i:4}{contador:16}{porcentagem:14.1f}%.')

print()
print(f'O melhor jogador foi o número {melhor_jogador}, com {maior_voto} votos, correspondendo a {melhor_porcentagem:.1f}% do total de votos.')

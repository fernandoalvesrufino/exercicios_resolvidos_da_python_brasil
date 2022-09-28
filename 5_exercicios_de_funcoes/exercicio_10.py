# Exercício 10 - Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
# Se, na primeira jogada, você tirar 7 ou 11, você é um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" 
# e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar 
# este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random

def dados():
  dado_1 = random.randrange(1, 7)
  dado_2 = random.randrange(1, 7)
  resultado = dado_1 + dado_2
  print(f'Resultado dos dados: {resultado}')
  return resultado


tentativa = 0
primeira_tentativa = 0

print('----------- VAMOS JOGAR CRAPS -----------')
print()
comecar = input('Para começar aperte ENTER!')

while True:
  tentativa += 1
  joga_dados = dados()

  if tentativa == 1:
    primeira_tentativa = joga_dados
    if (joga_dados == 7) or (joga_dados == 12):
      print('Você é um NATURAL! Parabéns, você ganhou o jogo!')
      print()
      break
    elif (joga_dados == 2) or (joga_dados == 3) or (joga_dados == 12):
      print('CRAPS! Você perdeu o jogo!')
      print()
      break
    else:
      print(f'{primeira_tentativa} é o seu PONTO! Tire {primeira_tentativa} de novo para ganhar. OBS: Você só não pode tirar 7 hein.')
      continuar = input('Jogue o dado novamente! Para isso aperte ENTER!')
      print()

  else:
    if (joga_dados == 7):
      print('Poxa, que pena. Você perdeu!')
      break
    else:
      if joga_dados == primeira_tentativa:
        print('Você repetiu seu ponto! Parabéns, você ganhou o jogo!')
        print()
        break
      else:
        continuar = input('Jogue o dado novamente! Para isso aperte ENTER!')
        print()

# Exercício 11 - Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!

# Digite uma letra: O
# A palavra é: _ _ _ _ O

# Digite uma letra: E
# A palavra é: _ E _ _ O

# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!

import random

letras_certas = []
letras_erradas = []
erros = 0
chance = 6

with open("sample_data/personagens.txt","r") as arquivo:
  allText = arquivo.read()
  modelos = list(map(str, allText.split())) 

  palavra = random.choice(modelos) 

palavra_lista = list(palavra)

print('----- JOGO DA FORCA -----')
print('Dica: ', end = '')

for i in range(len(palavra)):
  print('_', end = ' ')
print()
print()

while True:
  print(f'Chutes certos: {letras_certas}')
  print(f'Chutes errados: {letras_erradas}')
  print(f'Você tem {chance} chances!')
  letra = input('Chute uma letra: ').upper()
  if letra in palavra:
    letras_certas.append(letra)
  else:
    letras_erradas.append(letra)
    erros += 1
    chance -= 1

  
  for i in range(len(palavra)):
    if palavra[i] in letras_certas:
      print(palavra[i], end = ' ')
    else:
      print('_', end = ' ')
  
  print()
  print()

  if (set(palavra_lista) == set(letras_certas)):
    print('Parabéns! Você ganhou!')
    break


  if erros == 6:
    print('Enforcado! Você perdeu')
    break

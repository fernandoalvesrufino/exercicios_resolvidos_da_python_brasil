# Exercício 13 - Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. 
# O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra.
# Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

from random import sample
def embaralha(nome):
    a = sample(nome,len(nome))
    d = ''.join(a)
    return d.upper()


palavras_erradas = []
erros = 0
chances = 6

with open("sample_data/carros.txt","r") as arquivo:
  allText = arquivo.read()
  modelos = list(map(str, allText.split())) 

  palavra = random.choice(modelos).upper()

palavra_embaralhada = embaralha(palavra) 

palavra_lista = list(palavra_embaralhada)

print('----- DESCUBRA A PALAVRA -----')
print('Dica: ', end = '')

while True:
  print(f'A palavra embaralhada é {palavra_embaralhada}')
  print(f'Chutes errados: {palavras_erradas}')
  print(f'Você tem {chances} chances!')
  tentativa = input('Qual é a palavra certa? ').upper()
  if tentativa == palavra:
    print()
    print(f'Parabens! Você acertou! A palavra é {palavra}')
    break
  else:
    palavras_erradas.append(tentativa)
    erros += 1
    chances -= 1

  print()

  if erros == 6:
    print('Enforcado! Você perdeu')
    break

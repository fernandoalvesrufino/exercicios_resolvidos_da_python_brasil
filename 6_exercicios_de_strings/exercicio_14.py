# Exercício 14 - Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. 
# A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, 
# sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um 
# programa que peça uma texto e transforme-o para a grafia leet speak.

alfabeto_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabeto_lista = list(alfabeto_str)
traducao_lista = ['4','8','(','[)','3','|=','6','|-|','|',']','|<','1','|Y|','/\/','0','|>','0,','|2','5','7','|_|','\/','\v/','}{','/','2']

def leet_speak(palavra):
  nova_palavra = []
  lista_palavra = list(palavra)
  for i in range(len(palavra)):
    letra = palavra[i]
    posicao = alfabeto_lista.index(letra)
    nova_palavra.append(traducao_lista[posicao])
  
  traduzido = ' '.join(nova_palavra)
  return traduzido

  

print('------ TRADUZA PARA LEET SPEAK ------')
print()
palavra = input('Digite uma palavra: ').upper()
palavraleet = leet_speak(palavra)
print(palavraleet)

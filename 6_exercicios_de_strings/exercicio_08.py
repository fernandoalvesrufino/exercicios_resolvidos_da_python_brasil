# Exercício 8 - Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. 
# Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma 
# frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

caracteres = ' !?.,'

print('---------- PALÍNDROMO OU NÃO ----------')
frase = input('Digite uma palavra ou frase: ').upper()
print()
nova_frase = ''.join(i for i in frase if i not in caracteres)
frase_inversa = nova_frase[::-1]

if nova_frase == frase_inversa:
  print('É um palíndromo!')
else:
  print('Não é um palíndromo!')

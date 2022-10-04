# Exercício 7 - Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.

frase = input('Digite uma frase: ').upper()
vogais = ['A', 'E', 'I', 'O', 'U']
contador_vogal = 0

espacos = frase.count(' ')
for i in range(len(frase)):
  if frase[i] in vogais:
    contador_vogal += 1

print(f'''
Na sua frase aparecem {espacos} espaços e {contador_vogal} vogais
''')

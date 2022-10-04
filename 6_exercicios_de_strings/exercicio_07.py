# Exercício 7 - Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.

frase = input('Digite uma frase: ').upper()

espacos = frase.count(' ')
a = frase.count('A')
e = frase.count('E')
i = frase.count('I')
o = frase.count('O')
u = frase.count('U')
vogais = a + e + i + o + u

print(f'''
Na sua frase aparecem {espacos} espaços e {vogais} vogais
''')

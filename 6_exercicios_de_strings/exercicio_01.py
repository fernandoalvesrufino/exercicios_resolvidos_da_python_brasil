# Exercício 1 - Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

string_1 = input('Digite uma palavra: ')
string_2 = input('Digite outra palavra: ')

if len(string_1) == len(string_2):
  tamanho = 'iguais'
else:
  tamanho = 'diferentes'

if (string_1 in string_2) or (string_2 in string_1):
  if len(string_1) == len(string_2):
    conteudo = 'iguais'
  else:
    conteudo = 'diferentes'
else:
  conteudo = 'diferentes'

print(f'''
Palavra 1: {string_1}
Palavra 2: {string_2} 
Comprimento de "{string_1}": {len(string_1)} caracteres
Comprimento de "{string_2}": {len(string_2)} caracteres
As duas strings são de tamanhos {tamanho}.
As duas strings possuem conteúdo {conteudo}.
''')

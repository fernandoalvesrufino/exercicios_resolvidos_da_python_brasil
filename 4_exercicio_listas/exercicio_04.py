# Exercício 4 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

consoantes = []
vogais = ['A', 'E', 'I', 'O', 'U']

for i in range(5):
  letra = input('Digite uma letra: ').upper()
  if letra in vogais:
    pass
  else:
    consoantes.append(letra)

print(f'Foram digitadas {len(consoantes)} consoantes.')
print(f'As consoantes digitadas foram: {consoantes}.')

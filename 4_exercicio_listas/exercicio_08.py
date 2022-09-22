# Exercício 8 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []

for i in range (1, 4):
  anos = int(input(f'Informe a idade da {i}ª pessoa: '))
  idade.append(anos)
  centimetros = float(input(f'Informe a altura da {i}ª pessoa: '))
  altura.append(centimetros)

idade.reverse()
altura.reverse()

print()
print(idade)
print(altura)

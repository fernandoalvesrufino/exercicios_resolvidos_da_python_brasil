# Exercício 11 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor_1 = []
vetor_2 = []
vetor_3 = []
vetor_4 = []

for _ in range (5):
  numero = float(input('Digite um número do primeiro conjunto: '))
  vetor_1.append(numero)

print()

for _ in range (5):
  numero = float(input('Digite um número do segundo conjunto: '))
  vetor_2.append(numero)

print()

for _ in range (5):
  numero = float(input('Digite um número do segundo conjunto: '))
  vetor_3.append(numero)

print()

for i in range(5):
  vetor_4.append(vetor_1[i])
  vetor_4.append(vetor_2[i])
  vetor_4.append(vetor_3[i])

print(vetor_4)

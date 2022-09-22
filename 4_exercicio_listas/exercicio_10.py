# Exercício 10 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos 
# elementos intercalados dos dois outros vetores.

vetor_1 = []
vetor_2 = []
vetor_3 = []

for _ in range (5):
  numero = float(input('Digite um número do primeiro conjunto: '))
  vetor_1.append(numero)

print()

for _ in range (5):
  numero = float(input('Digite um número do segundo conjunto: '))
  vetor_2.append(numero)

print()

for i in range(5):
  vetor_3.append(vetor_1[i])
  vetor_3.append(vetor_2[i])

print(vetor_3)

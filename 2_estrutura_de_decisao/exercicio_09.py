# Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []

for i in range(3):
    number = float(input(f'Digite o {i + 1}º número: '))
    lista.append(number)

lista.sort(reverse=True)
print(lista)

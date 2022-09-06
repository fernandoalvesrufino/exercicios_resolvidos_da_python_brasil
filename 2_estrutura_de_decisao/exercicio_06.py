# Faça um Programa que leia três números e mostre o maior deles.

maior = -999999
for i in range(3):
    numero = float(input('Digite um número: '))
    if numero > maior:
        maior = numero
print(f'O maior valor digitado foi {maior}.')

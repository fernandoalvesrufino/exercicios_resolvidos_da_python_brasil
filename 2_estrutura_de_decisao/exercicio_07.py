# Faça um Programa que leia três números e mostre o maior e o menor deles.

numero = float(input('Digite um número: '))
maior = numero
menor = numero

for contador in range(2):
    outro_numero = float(input('Digite outro número: '))
    if outro_numero > maior:
        maior = outro_numero
    if outro_numero < menor:
        menor = outro_numero


print(f'O maior valor digitado foi {maior}.')
print(f'O menor valor digitado foi {menor}.')

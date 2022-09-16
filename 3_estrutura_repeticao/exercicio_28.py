# Exercício 28 - Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

cd = int(input('Quantos CDs você possui? '))
print()
soma = 0


for i in range(cd):
  valor = float(input(f'Qual o valor do {i + 1}º CD? R$ '))
  soma = soma + valor

media = soma / cd
print(f'Você já investiu R${soma:.2f} em CDs. O valor médio de cada CD é de R${media:.2f}')

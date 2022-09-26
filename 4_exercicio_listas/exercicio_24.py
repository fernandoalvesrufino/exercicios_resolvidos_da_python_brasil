# Exercício 24 - Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes 
# cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

import random

aleatorio = []

for i in range(100):
  numero = random.randint(1, 6)
  aleatorio.append(numero)

for i in range(1,7):
  print(f'{i} - {aleatorio.count(i)}')

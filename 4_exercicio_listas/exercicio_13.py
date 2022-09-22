# Exercício 13 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das
# temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperatura = []
meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO'] 

for i in range (1,13):
  temp = float(input(f'Informe a temperatura média do mês {i}: '))
  temperatura.append(temp)
  anual = sum(temperatura) / len(temperatura)

print()
print(f'A temperatura média anual foi de {anual} ºC.')
print()

for i in range(12):
  if temperatura[i] > anual:
    print(f'{i + 1} - {meses[i]} teve a temperatura média: {temperatura[i]} ºC.')

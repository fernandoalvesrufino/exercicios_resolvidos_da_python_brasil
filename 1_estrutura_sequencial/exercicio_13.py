# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input('Informe a altura da pessoa: '))
peso_ideal_homens = (72.7 * altura) - 58
peso_ideal_mulheres = (62.1 * altura) - 44.7
print(f'Para {altura:.2f}m de altura o peso ideal de um homem é de {peso_ideal_homens:.2f} Kg'
      f' e de uma mulher é de {peso_ideal_mulheres:.2f} Kg')

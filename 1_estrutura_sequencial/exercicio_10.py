# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input('Informe a temperatura em ºC: '))
fahrenheit = celsius * 1.8 + 32
print(f'A temperatura de {celsius:.1f}ºC corresponde a {fahrenheit:.1f}ºF!')

# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahrenheit = float(input('Informe a temperatura em ºF: '))
celsius = 5 * ((fahrenheit-32) / 9)
print(f'A temperatura de {fahrenheit:.1f}ºF corresponde a {celsius:.1f}ºC!')

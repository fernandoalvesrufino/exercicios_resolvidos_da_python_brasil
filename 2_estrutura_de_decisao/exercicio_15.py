# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes.

l1 = float(input('Informe o valor do primeiro lado: '))
l2 = float(input('Informe o valor do segundo lado: '))
l3 = float(input('Informe o valor do terceiro lado: '))

if ((l1 + l2) > l3) and ((l1 + l3) > l2) and ((l2 + l3) > l1):
    print('Pode ser um triângulo.')
    if (l1 == l2) and (l1 == l3) and (l2 == l3):
        print('É um Triângulo Equilátero.')
    elif (l1 != l2) and (l1 != l3) and (l2 != l3):
        print('É um Triângulo Escaleno.')
    else:
        print('É um Triângulo Isósceles.')
else:
    print('Não pode ser um triângulo.')

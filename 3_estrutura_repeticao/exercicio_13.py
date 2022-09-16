# Exercício 13 - Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem.

base = int(input('Informe o valor da base: '))
exp = int(input('Informe o valor do expoente: '))
resultado = 1

for i in range(exp):
   resultado *= base 

print(resultado)

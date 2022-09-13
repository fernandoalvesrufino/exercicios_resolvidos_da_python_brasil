# Exercício 5 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação.

anos = 0

a = float(input('Informe a quantidade de habitantes que há no país A: '))
b = float(input('Informe a quantidade de habitantes que há no país B: '))

taxa_a = float(input('Informe a taxa de crescimento anual (%) do país A: '))
taxa_b = float(input('Informe a taxa de crescimento anual (%) do país B: '))

while a <= b:
  a = a + (a * (taxa_a / 100))
  b = b + (b * (taxa_b / 100))
  anos += 1 

print()
print(f'Serão necessários {anos} anos para o país A ultrapassar ou igualar o país B.')

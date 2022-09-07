# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

day = int(input('Digite um número correspondente ao dia da semana: '))

if day == 1:
    print('Domingo')
elif day == 2:
    print('Segunda')
elif day == 3:
    print('Terça')
elif day == 4:
    print('Quarta')
elif day == 5:
    print('Quinta')
elif day == 6:
    print('Sexta')
elif day == 7:
    print('Sábado')
else:
    print('Valor inválido!')

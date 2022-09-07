# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M - matutino ou V - Vespertino
# ou N - Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Qual turno você estuda? [M] - Manhã, [T] - Tarde, [N] - Noite: ').upper()

if (turno == 'M') or (turno == 'MANHA'):
    print('Bom Dia!')
elif (turno == 'T') or (turno == 'TARDE'):
    print('Boa Tarde!')
elif (turno == 'N') or (turno == 'NOITE'):
    print('Boa Noite!')
else:
    print('Valor Inválido!')

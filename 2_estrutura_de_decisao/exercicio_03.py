# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Informe o sexo? [M] para Masculino ou [F] para Feminino: ').upper()
if (sexo == 'M'):
    print('O sexo Masculino foi selecionado.')
elif (sexo == 'F'):
    print('O sexo Feminino foi selecionado.')
else:
    print('Sexo inválido!')

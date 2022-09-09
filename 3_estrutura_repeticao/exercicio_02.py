# Exercício 2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
  nome = input('Informe seu nome: ')
  senha = input('Informe sua senha: ')

  if nome == senha:
    print('\nERRO! A sua senha não pode ser igual ao seu nome! Por favor, digite outra senha!')
  else:
    print('\nCadastro concluido com sucesso!')
    break
  

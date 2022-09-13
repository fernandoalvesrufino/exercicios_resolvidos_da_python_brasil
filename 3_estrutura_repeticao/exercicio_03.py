# Exercício 3 - Faça um programa que leia e valide as seguintes informações:

# - Nome: maior que 3 caracteres;
# - Idade: entre 0 e 150;
# - Salário: maior que zero;
# - Sexo: 'f' ou 'm';
# - Estado Civil: 's', 'c', 'v', 'd';

sexo_lista = ['F', 'M']
estado_civil_lista = ['S', 'C', 'V', 'D']

while True:
  nome = input('Nome: ')
  if len(nome) > 3:
    break
  else:
    print('Você deve informar um nome com no mínimo 3 caracteres!')

while True:
  idade = int(input('Idade: '))
  if 0 <= idade <= 150:
    break
  else:
    print('Informe uma idade válida! Entre 0 e 150 anos.')

while True:
  salario = float(input('Salário: R$ '))
  if salario > 0:
    break
  else:
    print('Informe um salário maior que 0!')

while True:
  sexo = input('Sexo: [M] / [F] ').upper()
  if sexo in sexo_lista:
    break
  else:
    print('Informe M para masculino ou F para feminino.')

while True:
  estado_civil = input('Estado civil: [S], [C], [V] ou [D] ').upper()
  if estado_civil in estado_civil_lista:
    break
  else:
    print('Informe S para solteiro, C para casado, V para viúvo ou D para divorciado!')
    

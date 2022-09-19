# Exercício 36 - Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente 
# iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:

numero = int(input('Quer ver a tabuada de qual número? '))

while True:
  inicio = int(input('A partir de: '))
  final = int(input('Ate: '))

  if final < inicio:
    print('Informe um valor de início menor que o de final!')
  else:
    break
print()
print(f'Vou montar a tabuada de {numero} começando em {inicio} e terminando em {final}:')
print()

for i in range(inicio, final + 1):
  resultado = i * numero
  print(f'{numero} x {i} = {resultado}')

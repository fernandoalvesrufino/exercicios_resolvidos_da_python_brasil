# Exercício 20 - Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial 
# a números inteiros positivos e menores que 16.

while True:
  numero = int(input('Digite um número que você deseja calcular o fatorial: '))
  if numero == -1:
    break

  elif 0 <= numero <= 16:
    for i in range((numero - 1), 1, -1):
      numero = numero * i
    print(numero)

  else:
    print('Informe um número entre 0 e 16. Ou digite -1 para sair!')
    print()


print()
print('Fim do programa!')

# Exercício 15 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).

# Após esta entrada de dados, faça:

# - Mostre a quantidade de valores que foram lidos;
# - Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# - Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# - Calcule e mostre a soma dos valores;
# - Calcule e mostre a média dos valores;
# - Calcule e mostre a quantidade de valores acima da média calculada;
# - Calcule e mostre a quantidade de valores abaixo de sete;
# - Encerre o programa com uma mensagem;

notas = []
numero = 0

while numero != -1:
  numero = float(input('Digite a última nota da prova: '))
  if numero != -1:
    notas.append(numero)

media = sum(notas) / len(notas)

print()

print(f'Quantidade de valores que foram lidos: {len(notas)}')
print(f'Valores na ordem informada: {notas}')
notas.reverse()
print(f'Valores na ordem inversa: {notas}')
print(f'Soma dos valores: {sum(notas)}')
print(f'Média dos valores: {media}')

cont = 0
abaixo = 0

for i in range(len(notas)):
  if notas[i] > media:
    cont += 1

print(f'Quantidade de valores acimada média: {cont}')

for i in range(len(notas)):
  if notas[i] < 7:
    abaixo += 1

print(f'Quantidade de valores abaixo de 7: {abaixo}')

print('Fim do programa!')

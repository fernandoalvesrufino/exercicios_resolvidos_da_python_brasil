# Exercício 6 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média 
# maior ou igual a 7.0.

alunos = []
media_alunos = []
aprovados = 0


for i in range(1,4):
  nome = input(f'Informe o nome do(a) {i} aluno(a): ')
  alunos.append(nome)
  notas = []
  for i in range(1,5):
    numero = float(input(f'Informe a {i}ª nota de {nome}: '))
    notas.append(numero)
  media = sum(notas) / len(notas)
  if media >= 7 :
    aprovados += 1
  media_alunos.append(media)
  print() 


print(alunos)
print(media_alunos)
print()

if aprovados == 0:
  print('Nenhum aluno foi aprovado.')
elif aprovados == 1:
  print(f'Apenas {aprovados} aluno tirou média maior que 7.')
else:
  print(f'{aprovados} alunos tiraram média maior que 7.')

# Exercício 27 - Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
# As turmas não podem ter mais de 40 alunos.

quantidade = 0
turma = int(input('Informe a quantidade de turmas: '))
print()

for i in range(turma):
  alunos = int(input(f'Quantos alunos tem na {i + 1}ª turma? '))
  quantidade = quantidade + alunos

media = quantidade / turma

print()
print(f'A média de alunos por turma é de {media} alunos.')

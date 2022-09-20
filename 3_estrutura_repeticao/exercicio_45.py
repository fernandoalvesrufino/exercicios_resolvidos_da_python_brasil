# Exercício 45 - Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada 
# questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar
# o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar: Maior e Menor Acerto; Total de Alunos
# que utilizaram o sistema; A Média das Notas da Turma. Gabarito da Prova:

# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
notas = []
alunos = 0
maior = 0
menor = 10

while True:
  acertou = 0
  for i in range(10):
    while True:
      resposta = input(f'Informe a resposta da {i + 1}ª questão: ').upper() 
      if resposta in gabarito:
        break
      else:
        print('Informe a alternativa selecionada na prova! A, B, C, D ou E.')
        print()
    if resposta == gabarito[i]:
      acertou += 1
  notas.append(acertou)
  alunos += 1

  continuar = input('Outro aluno vai utilizar o sistema? [S] / [N] ').upper()
  if (continuar == 'N') or (continuar == 'NÃO'):
    break

media = sum(notas) / alunos

for i in range(len(notas)):
  if notas[i] > maior:
    maior = notas[i]
  elif notas[i] < menor:
    menor = notas[i]

print(f'''
Maior acerto = {maior}
Menor acerto = {menor}
Total de alunos = {alunos} alunos
Média das notas = {media:.1f}
''')

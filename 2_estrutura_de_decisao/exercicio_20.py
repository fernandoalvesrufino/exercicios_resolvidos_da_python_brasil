# Exercício 20 - Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

# - A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# - A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# - A mensagem "Aprovado com Distinção", se a média for igual a 10.

n1 = int(input('Informe a primeira nota: '))
n2 = int(input('Informe a segundaa nota: '))
n3 = int(input('Informe a terceira nota: '))

soma = n1 + n2 + n3
media = soma / 3
print()

if media < 7:
  print('REPROVADO!')
elif 7 <= media < 10:
  print('APROVADO.')
elif media == 10:
  print('APROVADO COM DISTINÇÃO!')

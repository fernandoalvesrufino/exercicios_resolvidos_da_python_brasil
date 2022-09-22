# Exercício 12 - Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior 
# à média de altura desses alunos.

idades = []
alturas = []
contador = 0

for i in range (1, 6):
  anos = int(input(f'Quantos anos o aluno {i} tem? '))
  tamanho = float(input(f'Qual é a altura do aluno {i}? '))
  idades.append(anos)
  alturas.append(tamanho)

print()
media_alturas = sum(alturas) / len(alturas)
print(f'A altura média é: {media_alturas:.2f} m.')

for i in range(5):
  if (idades[i] > 13) and (alturas[i] < media_alturas):
    contador += 1

print(f'Existem {contador} alunos com MAIS DE 13 anos e com altura INFERIOR à altura média dos alunos.')

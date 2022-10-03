# Exercício 4 - Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

# F
# FU
# FUL
# FULA
# FULAN
# FULANO

nome = input('Digite um nome: ').upper()

for i in range(len(nome) + 1):
  for _ in range(i):
    print(nome[_], end = '')
  print()

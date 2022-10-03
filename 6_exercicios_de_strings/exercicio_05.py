# Exercício 5 - Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

# FULANO
# FULAN
# FULA
# FUL
# FU
# F

nome = input('Digite um nome: ').upper()

for i in range(len(nome)):
  for _ in range(len(nome) - i):
    print(nome[_], end = '')
  print()

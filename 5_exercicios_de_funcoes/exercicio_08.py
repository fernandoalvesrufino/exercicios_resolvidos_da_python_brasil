# Exercício 8 - Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def quantidade_digitos(numero):
  int_to_str = str(numero)
  return len(int_to_str)


quantidade_1 = quantidade_digitos(234872384)
print(quantidade_1)

# Exercício 9 - Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(n):
  int_to_str = str(n)
  revertido = int_to_str[::-1]
  str_to_int = int(revertido)
  return str_to_int

inverter = reverso(456)
print(inverter)

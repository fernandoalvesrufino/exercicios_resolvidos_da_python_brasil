# Exercício 13 - Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros,
# linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser 
# modificados para valores dentro da faixa de forma elegante.

def omissao(tracos):
  if tracos == '':
    return 1
  elif tracos == 0:
    return 1
  elif tracos > 20:
    return 20
  else:
    return tracos


def desenhar_largura(c):
  print('+', end = '')
  print('-' * c, end = '')
  print('+')

def desenhar_altura(l, c):
  for i in range(l):
    print('|', end = '')
    print(' ' * c, end = '')
    print('|')

def retangulo(colunas, linhas):
  desenhar_largura(colunas)
  desenhar_altura(linhas, colunas)
  desenhar_largura(colunas)


colunas = int(input('Colunas: '))
linhas = int(input('Linhas: '))
c = omissao(colunas)
l = omissao(linhas)
retangulo(c, l)

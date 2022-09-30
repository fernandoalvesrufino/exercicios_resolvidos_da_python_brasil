# Exercício 11 - Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso 
# de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def data(dd, mm, aaaa):
  cont = 0
  ano = str(aaaa)
  if 0 < dd <= 31:
    dia_valido = dd
    cont += 1
  if 0 < mm <= 12:
    mes_valido = meses[mm - 1]
    cont += 1
  if len(ano) == 4:
    ano_valido = aaaa
    cont += 1

  if cont == 3:
    return f'{dia_valido} de {mes_valido} de {ano_valido}'
  else:
    return 'NULL'


d = int(input('Dia: '))
m = int(input('Mês: '))
a = int(input('Ano: '))
converter = data(d, m, a)
print(converter)

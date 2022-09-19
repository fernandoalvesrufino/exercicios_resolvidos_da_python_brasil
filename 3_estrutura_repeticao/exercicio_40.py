# Exercício 40 - Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

# - Código da cidade;
# - Número de veículos de passeio (em 1999);
# - Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# - Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# - Qual a média de veículos nas cinco cidades juntas;
# - Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

codigo = 0
quantidade = 0
acidentes = 0
maior = 0
menor = 999999999
total_veiculos = 0
total_acidentes = 0
codigo_maior = 0
codigo_menor = 0
contador = 0
media_veiculos = 0
media_acidentes = 0
continuar = 'S'

for i in range(5):
  codigo = int(input('Informe o código da cidade: '))
  quantidade = int(input('Informe a quantidade de veículos que existe na cidade: '))
  acidentes = int(input('Quantos acidentes ocorreram em 1999? '))
  
  if acidentes > maior:
    maior = acidentes
    codigo_maior = codigo
  if acidentes < menor:
    menor = acidentes
    codigo_menor = codigo

  total_veiculos += quantidade
  total_acidentes += acidentes
  print()

media_veiculos = total_veiculos / 5
media_acidentes = total_acidentes / 5

print(f'''
O maior indice de acidentes foi igual a {maior} na cidade {codigo_maior}.
O menor indice de acidentes foi igual a {menor} na cidade {codigo_menor}.
A média de veículos das cinco cidades é de {media_veiculos}
A média de acidentes das cinco cidades é de {media_acidentes}
''')

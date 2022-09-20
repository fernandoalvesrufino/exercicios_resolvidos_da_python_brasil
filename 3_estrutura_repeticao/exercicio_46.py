# Exercício 46 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior 
# resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias
# alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular 
# a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado 
# quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

from typing import List

atleta = []
media_salto = []
nome = 'Start'
contagem = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
salto: list[float] = []
saltos_dos_atletas = []

while True:
    menor = 999999
    maior = 0
    nome = input('Atleta: ')
    print()
    if nome == '':
        break
    else:
        atleta.append(nome)
        media = 0
        salto_do_atleta = 0

        for i in range(5):
            distancia_salto = float(input(f'{contagem[i]} salto: '))
            salto.append(distancia_salto)
        for s in range(len(salto)):
            if salto[s] > maior:
                maior = salto[s]
            if salto[s] < menor:
                menor = salto[s]
        salto.remove(maior)
        salto.remove(menor)
        print()
        print(f'Melhor salto: {maior:.1f} m')
        print(f'Pior salto: {menor:.1f} m')
        salto_do_atleta += sum(salto)
        media = salto_do_atleta / 3
        media_salto.append(media)
        print(f'Média dos demais saltos: {media:.2f} m')

    print()

# valores_saltos = ' - '.join(map(str, salto))

inicio = 0
fim = 3

for i in range(len(atleta)):
    print('Resultado final:')
    print(f'Atleta: {atleta[i]}')
    saltos_dos_atletas.clear()
    # for i1 in range(len(salto))

    for _ in range(inicio, fim):
        saltos_dos_atletas.append(salto[_])

    inicio += 5
    fim += 5
    valores_saltos = ' - '.join(map(str, saltos_dos_atletas))
    print()
    print(f'Saltos: {valores_saltos}')
    print(f'Média dos saltos: {media_salto[i]:.2f} m')
    print()
